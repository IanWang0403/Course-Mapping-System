var g = new dagreD3.graphlib.Graph()
  .setGraph({})
  .setDefaultEdgeLabel(function() { return {}; });

var svg = d3.select("svg"),
  inner = svg.append("g");

d3.csv("database_test.csv").then(function(data) {

  for (var i = 0; i < data.length; i++) {
    g.setNode(data[i].course_id, {label: data[i].course_name, description: data[i].course_detail})
  }

  for (var i = 0; i < data.length; i++) {
      if(data[i].course_pr.search(/, | or |; | and /) == -1){
        if(g.hasNode(data[i].course_pr)){
          g.setEdge(data[i].course_pr, data[i].course_id, {
            curve: d3.curveBasis 
          });

        }
      }
      else{
        tmpData = data[i].course_pr.split(/, | or |; | and /);
        
        for(var j = 0; j < tmpData.length; j++){
          
          if(g.hasNode(tmpData[j])){
            if(data[i].course_pr.search("and") != -1){
              g.setEdge( tmpData[j], data[i].course_id,{
                curve: d3.curveBasis,
                arrowheadStyle: "fill :#f66"
              });
            }else{
              g.setEdge( tmpData[j], data[i].course_id, {
                curve: d3.curveBasis,
              });
            }
            

          }
        }
      }   
  }

  g.graph().rankDir = 'LR';
  g.graph().align = 'UR'
  g.graph().nodesep = 10;
  g.graph().edgesep = 10;
  g.graph().ranksep = 200
  //g.graph().ranker = "longest-path";

  var zoom = d3.zoom().on("zoom", function() {
    inner.attr("transform", d3.event.transform);
  });
  svg.call(zoom);

  var styleTooltip = function(name ,code, description) {
    return "<p class='name'>" + name + "</p><p class='code'>" + code + "</p><p class='description'>" + description + "</p>";
  };

  var render = new dagreD3.render();

  render(inner, g);

  inner.selectAll("g.node")
    .attr("code", function(v){return v})

  inner.selectAll("g.node")
    .attr("title", function(v) { return styleTooltip(g.node(v).label, v, g.node(v).description) })
    .each(function(v) { $(this).tipsy( { gravity: "n", opacity: 0.8, html: true }); });
    

  inner.selectAll("g.node").each(function(v){$(this).tipsy('disable')});

  var initialScale = 0.25;
  svg.call(zoom.transform, d3.zoomIdentity.translate((svg.attr("width") - g.graph().width * initialScale) / 2, 20).scale(initialScale));
  svg.attr("height", g.graph().height + 40);
  
});
