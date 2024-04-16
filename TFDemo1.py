import tensorflow as tf
from keras import ops
import pandas as pd
import numpy as np

class TFDemo:

    ds = None
    model = None
    def __init__(self):
        self.model = None

    def modelSetup(self) -> tf.keras.Model:
        self.model = tf.keras.models.Sequential([
            tf.keras.layers.Dense(units=10, activation="relu", name="L1"),
            tf.keras.layers.Dense(units=10, activation="relu", name="L2"),
            tf.keras.layers.Dense(units=1,  name="L3")
        ], name="Model-R")

        self.model.compile(optimizer='adam', loss=tf.keras.losses.MeanSquaredError(), metrics=['accuracy'])

        
        
    """def ann(self):
        model = TFDemo().modelSetup()
        x = ops.ones((1,5))
        y = model(x)
        print((model.summary()))
        print((model.trainable_weights))"""
        
    def read_load_csv(self) -> pd.DataFrame:
     self.ds = pd.read_csv("./my_data.csv")
     
     return self.ds   


tfdemo = TFDemo()
tfdemo.modelSetup()
m = tfdemo.model
csv_data = tfdemo.read_load_csv()
csv_data_cp = csv_data.copy()
csv_data_cp= csv_data_cp.replace('F',1)
csv_data_cp = csv_data_cp.replace('M',0)
lables = csv_data_cp.pop("BMI")
print(np.array(csv_data_cp))
print(lables)
m.fit(np.array(csv_data_cp), lables,
           epochs=10)

