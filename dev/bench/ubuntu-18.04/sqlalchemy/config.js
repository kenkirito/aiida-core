window.CONFIGURATION_DATA = {
    "suites": {
        "pytest-benchmarks:ubuntu-18.04,django": {
            "header": "Performance Benchmarks (Ubuntu-18.04, Django)",
            "description": "Performance benchmark tests, generated using pytest-benchmark."
        },
        "pytest-benchmarks:ubuntu-18.04,sqlalchemy": {
            "header": "Performance Benchmarks (Ubuntu-18.04, SQLAlchemy)",
            "description": "Performance benchmark tests, generated using pytest-benchmark."
        }
    },
    "groups": {
        "node": {
            "header": "Single Node",
            "description": "Comparison of basic node interactions, such as storage and deletion from the database.",
            "single_chart": true,
            "xAxis": "id",
            "backgroundFill": false
        },
        "engine-run": {
            "header": "Local Processes",
            "description": "Comparison of Processes, executed via a local runner.",
            "single_chart": true,
            "xAxis": "id",
            "backgroundFill": false
        }
    }
}
