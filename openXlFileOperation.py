import openpyxl
wb=openpyxl.Workbook()
sheet=wb.active
sheet['A1']=400
sheet['A2']=340
sheet['A3']=470
sheet['A4']=220
sheet['A5']=390
sheet['A6']='=sum(A1:A5)'
wb.save('excelSum2.xlsx')