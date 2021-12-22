import logging
import churn_library as churn


logging.basicConfig(
    filename='./logs/churn_library.log',
    level = logging.INFO,
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s')


def test_import(import_data):
	'''
	test data import - this example is completed for you to assist with the other test functions
	'''
	try:
		df = import_data(r"./data/bank_data.csv")
		logging.info("Testing import_data: SUCCESS")
	except FileNotFoundError as err:
		logging.error("Testing import_eda: The file wasn't found")
		raise err
	try:
		assert df.shape[0] > 0
		assert df.shape[1] > 0
	except AssertionError as err:
		logging.error("Testing import_data: The file doesn't appear to have rows and columns")
		raise err


def test_eda(perform_eda):
	'''
	test perform eda function
	'''
	try:
		perform_eda(df)
		logging.info("Testing perform_eda: SUCCESS")
	except TypeError as err:
		logging.error("Testing import_data: Input data is not a pandas dataframe")
		raise err
	try:
		'Attrition_Flag' in df.columns
		logging.info("Testing perform_eda: SUCCESS")
	except KeyError as err:
		logging.error("Testing import_data: Churn flag is not found")
		raise err
	try:
		cols = ['Gender','Education_Level','Marital_Status','Income_Category','Card_Category',
				'Dependent_count', 'Total_Relationship_Count', 'Months_Inactive_12_mon',
				'Contacts_Count_12_mon', 'Customer_Age','Months_on_book','Credit_Limit',
                'Total_Revolving_Bal','Avg_Open_To_Buy','Total_Amt_Chng_Q4_Q1','Total_Trans_Amt',
                'Total_Trans_Ct','Total_Ct_Chng_Q4_Q1','Avg_Utilization_Ratio']
		set(cols).intersection(set(df.columns)) == len(cols)
		logging.info("Testing perform_eda: SUCCESS")
	except KeyError as err:
		logging.error("Testing import_data: Not all X variable columns found")
		raise err


def test_encoder_helper(encoder_helper):
	'''
	test encoder helper
	'''


def test_perform_feature_engineering(perform_feature_engineering):
	'''
	test perform_feature_engineering
	'''


def test_train_models(train_models):
	'''
	test train_models
	'''


if __name__ == "__main__":
	test_import(churn.import_data)
	df = churn.import_data("./data/bank_data.csv")
	test_eda(churn.perform_eda)