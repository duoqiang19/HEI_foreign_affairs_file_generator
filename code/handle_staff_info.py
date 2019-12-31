import xlrd, datetime
#import xlwt

class Handle_staff_data():

    def __init__(self,address):
        self.address = address
        self.book = xlrd.open_workbook(self.address)
        self.sheet = self.book.sheet_by_name(self.book.sheet_names()[0])
        self.datas = []
        for rowno in range(2,self.sheet.nrows):
            self.data = {}
            for colno in range(0,self.sheet.ncols):
                self.data[self.sheet.cell(1,colno).value] = self.sheet.cell(rowno,colno).value
            self.data['age'] = datetime.datetime.now().year - xlrd.xldate_as_tuple(self.data['birthday'],0)[0]
            #self.data['age'] = self.data['birthday']
            self.datas.append(self.data)

    def get_group_info(self,names):
        #data_output = {}
        #all_staff = self.sheet.col_values(3)[2:]
        all_staff_no = int(self.sheet.col_values(0)[-1])
        group = []
        if all_staff_no != self.sheet.nrows-2:
            return 1
        else:
            for name in names:
                for data in self.datas:
                    if name == data['name']:
                        group.append(data)
            return group

if __name__ == '__main__':

    import os
    staff_data_input = ['王多强']
    folder_path = os.path.abspath(os.path.dirname(os.getcwd()))
    staff_info_address = str(folder_path + "/database/" + "staff_info.xls").replace("\\","/")
    x = Handle_staff_data(staff_info_address)
    print(x.get_group_info(staff_data_input))

