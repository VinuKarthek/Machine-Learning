from locust import HttpUser, task, between

class MLClassifierUser(HttpUser):
    # Define the host

    # Wait time between tasks
    wait_time = between(1, 3)

    @task
    def index_page(self):
        self.client.get("/")

    @task
    def predict_affluent(self):
        # Define the JSON payload
        payload = {
            "C_AGE": 0, 
            "C_EDU": '', 
            "C_HSE": '' ,
            "INCM_TYP": 0,
            "gn_occ": '',
            "NUM_PRD": 0,
            "CASATD_CNT": 0,
            "MTHCASA": 0, 
        }

        # Make the POST request
        self.client.post("/predict/affluent", json=payload)