# ScyllaDB Prometheus metrics

This script fetches the list of metrics from a ScyllaDB server and generates a single page HTML documentation for all the metrics.

### Running locally

- Clone this repository.
- To generate from ScyllaDB, run `python3 generate.py http://scylla-url:9180/metrics > index.html`
- To generate from a file with metrics dumped in it, run `python3 generate.py ./metrics_file > index.html`
