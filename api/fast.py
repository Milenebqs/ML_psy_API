import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from xxx import load_model

app = FastAPI()
app.state.model = load_model()

# Allowing all middleware (optional but good practice for dev purposes)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Implementing the root endpoint /
@app.get("/")
def root():
    return {'ML Psy': '🔥🔥🔥'}


# Implement the rood predict to get prediction from the imported model
@app.get("/predict")
def predict(df: pd.DataFrame) -> str:
    """
    Make a single prediction of mental disorder
    """
    # X_pred = pd.DataFrame(locals(),index=[3])
    # X_pred['pickup_datetime'] = pd.Timestamp(pickup_datetime, tz='US/Eastern')
    # print(X_pred)

    # assert app.state.model is not None

    # X_processed = preprocess_features(X_pred)
    # y_pred = app.state.model.predict(X_processed)

    # return {'fare':float(y_pred)}
