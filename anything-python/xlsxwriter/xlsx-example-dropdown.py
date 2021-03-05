import argparse
import pandas as pd
import xlsxwriter



def column_name_2_label(df, column_name):
    
    column_idx = list(df.columns).index(column_name)
    column_label = xlsxwriter.utility.xl_col_to_name(column_idx)
    
    return column_label

def main(args):
	df = pd.read_csv(args.path, sep='\t', encoding='utf-8')
	df = df.loc[:100, :].copy()
	df['qc_result'] = None

	# Create a Pandas Excel writer using XlsxWriter as the engine.
	output_name = args.output_name
	writer = pd.ExcelWriter(output_name, engine='xlsxwriter', options={'strings_to_formulas': False})

	# Convert the dataframe to an XlsxWriter Excel object.
	df.to_excel(writer, sheet_name='Sheet1', index=False, encoding='utf-8')

	# Get the xlsxwriter objects from the dataframe writer object.
	workbook  = writer.book
	worksheet = writer.sheets['Sheet1']

	# Apply dropdown
	col_label = column_name_2_label(df, 'qc_result')
	cell_range = "{0}{1}:{0}{2}".format(col_label, 1, len(df)+1)
	worksheet.data_validation(cell_range, {'validate': 'list', 'source': ['ACCEPT', 'REJECT']})

	# Save Excel file
	writer.save()


if __name__ == "__main__":

	parser = argparse.ArgumentParser(description="Input data path")
	
	parser.add_argument("--path", type=str, help="path to data file", required=True)
	parser.add_argument("--output_name", type=str, help="output file name", required=True)

	args = parser.parse_args()
	
	assert args.output_name[-5:] == ".xlsx", "Output file name must include '.xlsx' in the end"

	main(args)

