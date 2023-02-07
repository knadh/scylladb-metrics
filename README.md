<a href="https://zerodha.tech"><img src="https://zerodha.tech/static/images/github-badge.svg" align="right" /></a>


# ScyllaDB Prometheus metrics

This script fetches the list of metrics from a ScyllaDB server and generates a single page HTML documentation for all the metrics.

See the docs at [**knadh.github.io/scylladb-metrics**](https://knadh.github.io/scylladb-metrics/)

### Running locally

- Clone this repository.
- To generate from ScyllaDB, run `python3 generate.py http://scylla-url:9180/metrics > index.html`
- To generate from a file with metrics dumped in it, run `python3 generate.py ./metrics_file > index.html`
