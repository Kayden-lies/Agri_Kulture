(async()=>{const metrics=await (await fetch('/metrics')).json();const a=await (await fetch('/analytics')).json();
const labels=Object.keys(metrics);const acc=labels.map(k=>metrics[k].accuracy);new Chart(document.getElementById('metricsChart'),{type:'bar',data:{labels,datasets:[{label:'Accuracy',data:acc}]}});
const p=a.pca_points.slice(0,1200);new Chart(document.getElementById('pcaChart'),{type:'scatter',data:{datasets:[{label:'PCA',data:p.map(x=>({x:x.x,y:x.y}))}]}});
const c=a.clusters.slice(0,1200);new Chart(document.getElementById('clusterChart'),{type:'scatter',data:{datasets:[{label:'Clusters',data:c.map(x=>({x:x.temp,y:x.rainfall}))}]}});
})();
