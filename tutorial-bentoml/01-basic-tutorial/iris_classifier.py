import pandas as pd

from bentoml import env, artifacts, api, BentoService
from bentoml.adapters import DataframeInput
from bentoml.frameworks.sklearn import SklearnModelArtifact



@env(infer_pip_packages=True)                   # 이 모델을 만드는데 필요한 패키지를 requirements.txt 로 자동 생성
@artifacts([SklearnModelArtifact('model')])
class IrisClassifier(BentoService):
    """
    A minimum prediction service exposing a Scikit-learn model
    """

    @api(input=DataframeInput(), batch=True)
    def predict(self, df: pd.DataFrame):
        """
        An inference API named `predict` with Dataframe input adapter, which codifies
        how HTTP requests or CSV files are converted to a pandas Dataframe object as the
        inference API function input
        """
        return self.artifacts.model.predict(df)



# Firstly, the @artifact(...) here defines the required trained models
# to be packed with this prediction service. BentoML model artifacts are
# pre-built wrappers for persisting, loading and running a trained model.


# The @env decorator specifies the dependencies and environment settings
# required for this prediction service. It allows BentoML to reproduce the
# exact same environment when moving the model and related code to production.
# With the infer_pip_packages=True flag, BentoML will automatically find all
# the PyPI packages that are used by the prediction service code and pins their versions.


# The @api decorator defines an inference API, which is the entry point for
# accessing the prediction service. The input=DataframeInput() means this
# inference API callback function defined by the user, is expecting a pandas.DataFrame
# object as its input.