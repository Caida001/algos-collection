function topologicalSort(jobs, deps) {
  // Write your code here.
	const graph = createGraph(jobs, deps);
	return getOrderedJobs(graph);
}

function createGraph(jobs, deps) {
	const graph = new Graph(jobs);
	for(const [job, dep] of deps) {
		graph.addDeps(job, dep);
	}
	return graph;
}

function getOrderedJobs(graph) {
	const orderedJobs = [];
	const nodesWithNoPrereq = graph.nodes.filter(node => !node.numOfPrereqs);
	while(nodesWithNoPrereq) {
		const node = nodesWithNoPrereq.pop();
		orderedJobs.push(node.job);
		removeDeps(node, nodesWithNoPrereq);
	}
	const graphHasEdges = graph.nodes.some(node => node.numOfPrereqs);
	return graphHasEdges ? [] : orderedJobs;
}

function removeDeps(node, nodesWithNoPrereq) {
	while(node.deps.length) {
		const dep = node.deps.pop();
		dep.numOfPrereqs--;
		if(!dep.numOfPrereqs) nodesWithNoPrereq.push(dep);
	}
}

class Graph {
	constructor(jobs) {
		this.nodes = [];
		this.graph = {};
		for(const job of jobs) {
			this.addNode(job);
		}
	}

	addDeps(job, dep) {
		const jobNode = this.getNode(job);
		const depNode = this.getNode(dep);
		jobNode.deps.push(depNode);
		depNode.numOfPrereqs++;
	}

	addNode(job) {
		this.graph[job] = new JobNode(job);
		this.nodes.push(this.graph[job]);
	}

	getNode(job) {
		if(!(job in this.graph)) return this.addNode(job);
		return this.graph[job];
	}

}

class JobNode {
	constructor(job) {
	  this.job = job;
		this.deps = [];
		this.numOfPrereqs = 0;
	}

}
