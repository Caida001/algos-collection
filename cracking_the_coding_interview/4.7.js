// Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of
// projects, where the second project is dependent on the first project). All of a project's dependencies
// must be built before the project is. Find a build order that will allow the projects to be built. If there
// is no valid build order, return an error.
// EXAMPLE
// Input:
// projects: a, b, c, d, e, f
// dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
// Output: f, e, a, b, d, c

var Graph = require('./../util/Graph');

Graph.prototype.findNodeWithNoChildren = function() {
  for (var node in this.nodes) {
    if (Object.keys(this.nodes[node]).length === 0) {
      return node;
    }
  }
  return undefined;
};

var buildOrder = function(projects, dependencies) {
  var graph = new Graph();
  projects.forEach(project => {
    graph.addNode(project);
  });
  dependencies.forEach(dependency => {
    graph.addEdge(dependency[1], dependency[0]);
  });
  var answer = [];
  var currNode = graph.findNodeWithNoChildren();
  while (currNode !== undefined) {
    answer.push(currNode);
    graph.removeNode(currNode);
    currNode = graph.findNodeWithNoChildren();
  }
  if (answer.length === projects.length) {
    return answer;
  } else {
    throw Error;
  }
};

/* TEST */
var projects = ['a', 'b', 'c', 'd', 'e', 'f'];
var dependencies = [['a', 'd'], ['f', 'b'], ['b', 'd'], ['f', 'a'], ['d', 'c']];

console.log(buildOrder(projects, dependencies));
