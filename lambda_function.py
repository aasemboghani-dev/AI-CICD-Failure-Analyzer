import json

def lambda_handler(event, context):
    print("AI CI/CD Failure Analyzer received an event")

    body = event.get("body", event)

    if isinstance(body, str):
        try:
            body = json.loads(body)
        except json.JSONDecodeError:
            body = {}

    failure_log = body.get("failure_log", "")

    if "assert 200 == 500" in failure_log:
        root_cause = "The pytest expected HTTP 500, but the Flask application returned HTTP 200."
        recommended_fix = "Change the test assertion from status_code == 500 back to status_code == 200."
    elif "FAILED" in failure_log or "ERROR" in failure_log:
        root_cause = "The CI/CD pipeline encountered a test or build failure."
        recommended_fix = "Review the failed test or build stage and correct the underlying issue."
    else:
        root_cause = "Unable to identify a specific root cause from the provided log."
        recommended_fix = "Review the Jenkins console log for the failed stage."

    result = {
        "status": "analyzed",
        "root_cause": root_cause,
        "recommended_fix": recommended_fix,
        "failure_log": failure_log
    }

    print(json.dumps(result))

    return {
        "statusCode": 200,
        "body": json.dumps(result)
    }
