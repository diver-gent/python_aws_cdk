from aws_cdk import core

from my_custom_resource import MyCustomResource


# A Stack that sets up MyCustomResource and shows how to get an
# attribute from it.

class MyStack(core.Stack):
    def __init__(self, scope: core.App, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        resource = MyCustomResource(
            self, "python_aws_cdk_resource",
            Message="python_aws_cdk_resource says whaddup.",
        )

        # Publish the custom resource output
        core.CfnOutput(
            self, "ResponseMessage",
            description="This is a message from the python_aws_cdk Custom Resource",
            value=resource.response,
        )


app = core.App()
MyStack(app, "python-aws-cdk")
app.synth()
