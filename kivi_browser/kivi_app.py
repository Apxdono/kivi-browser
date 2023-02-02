import npyscreen as nps

class myEmployeeForm(nps.Form):
     def create(self):
        self.myName        = self.add(nps.TitleText, name='Name')
        self.myDepartment = self.add(nps.TitleSelectOne, scroll_exit=True, max_height=3, name='Department', values = ['Department 1', 'Department 2', 'Department 3'])
        self.myDate        = self.add(nps.TitleDateCombo, name='Date Employed')

class KiviApp(nps.NPSAppManaged):
	def onStart(self):
		self.addForm('MAIN', myEmployeeForm, name='New Employee')


def main():
	KiviApp().run()
	print("ohoho")

if __name__ == "__main__":
	main()
