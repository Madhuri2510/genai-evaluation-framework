import mlflow

mlflow.set_tracking_uri("file:./mlruns")
mlflow.set_experiment("GenAI_Evaluation")


def log_experiment(query, response, evaluation, config=None):
    with mlflow.start_run():

        mlflow.log_param("query", query)
        mlflow.log_param("response_length", len(response))

        if config:
            for key, value in config.items():
                mlflow.log_param(key, value)

        scores = evaluation["scores"]

        for metric, value in scores.items():
            if isinstance(value, (int, float)) and value is not None:
                mlflow.log_metric(metric, value)

        mlflow.log_param("verdict", evaluation["verdict"])