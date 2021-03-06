'use strict';

var fs = require('fs');
var crawler = require('hobbes-network-format');
var data = '/Users/jrmerz/dev/watershed/calvin-network-data/data';

var network = {
  type : 'FeatureCollection',
  features : []
};
var regions = {
  type : 'FeatureCollection',
  features : []
};


crawler(data, {parseCsvData : false}, function(results){

  results.nodes.features.forEach(function(node){
    network.features.push({
      $ref : node.properties.repo.dir.replace(data,'')+'/'+node.properties.repo.filename
    });
  });

  results.regions.features.forEach(function(node){
    if( !node.path ) return;

    regions.features.push({
      $ref : node.path.replace(data+'/', '')+'/region.geojson'
    });
  });


  if( fs.existsSync(data+'/network.geojson') ) {
    fs.unlinkSync(data+'/network.geojson');
  }
  if( fs.existsSync(data+'/regions.geojson') ) {
    fs.unlinkSync(data+'/regions.geojson');
  }

  fs.writeFileSync(data+'/network.geojson', JSON.stringify(network, '  ','  '));
  fs.writeFileSync(data+'/regions.geojson', JSON.stringify(regions, '  ','  '));

});
