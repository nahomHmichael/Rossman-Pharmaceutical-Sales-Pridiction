from prophet import Prophet
import pickle
import datetime
from prophet.diagnostics import cross_validation
from prophet.diagnostics import performance_metrics


class Fb_prophet:
    def __init__(self,train,holidays):
        self.future_dates = None
        self.forecast = None
        
        self.model = Prophet(interval_width = 0.95, holidays = holidays)
        self.model.fit(train)

          # dataframe that extends into future 6 weeks 
    def getFuture_dates(self,week):
        self.future_dates = self.model.make_future_dataframe(periods = int(week)*7)
        return self.future_dates
    def get_predicate(self):
        # predictions
        self.forecast = self.model.predict(self.future_dates)
       
        self.forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
        fc = self.forecast[['ds', 'yhat']].rename(columns = {'ds': 'Date', 'yhat': 'Forecast_Sales'})
        
        return fc
    def eff_modlel(self):
        # visualizing predicions
        fig1 = self.model.plot(self.forecast)
        fig1.savefig('forecastS.png')
    def get_components(self):
        fig2=self.model.plot_components(self.forecast)
        fig2.savefig('forecastComponents.png')
    def get_performanceMetrics(self):
        cross_validation_results = cross_validation(self.model, initial='370 days', period=3*7, horizon='70 days')
        print(cross_validation_results)

        performance_metrics_results = performance_metrics(cross_validation_results)
        return performance_metrics_results
    def save_model(self):
        now = datetime.datetime.now().strftime('%d-%m-%Y-%H-%M-%S-%f')[:-3]
        # Saving model to disk
     
        filename = now + '.pkl'
        path = '../models/' + filename
        pickle.dump(self.model, open(path, 'wb'))
        print('Saving model successful!!!')
        return filename