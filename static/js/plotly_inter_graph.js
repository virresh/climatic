x = document.getElementById("year").innerHTML
Plotly.d3.csv('/'+x, function(err, rows){
      function unpack(rows, key) {
          return rows.map(function(row) { return row[key]; });
      }
 console.log(unpack(rows, 'postal'));
 var data = [{
              type: 'choropleth',
              locationmode: 'country names',
              locations: unpack(rows, 'location'),
              z: unpack(rows, 'temp'),
              text: unpack(rows, 'location'),
              autocolorscale: true
          }];

  var layout = {
          title: 'HeatMap for year '+x,
          geo: {
            projection: {
              type: 'robinson'
            }
          }
      };
      Plotly.plot(myDiv, data, layout, {showLink: false});
  });
