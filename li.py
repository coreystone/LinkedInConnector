# TO RECOMPILE THE DESIGNER: pyuic5 -x LinkedIn_UI.ui -o ui.py
# TO COMPILE NEW IMAGES: pyrcc5 -o src_rc.py src.qrc

import sys
import subprocess
from linkedin import LinkedIn
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5 import uic, QtGui

Ui_MainWindow, QtBaseClass = uic.loadUiType('LinkedIn_UI.ui')

class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.current_person = self.get_person_selected()
        self.person_dict = {'Mark W' : ('mw', 'SANITIZED'),
                            'Hector S' : ('hs', 'SANITIZED'),
                            'Steve H' : ('sh', 'SANITIZED'),
                            'George L' : ('gl', 'SANITIZED'),
                            'Chris C' : ('cc', 'SANITIZED'),
                            'Gunnar L' : ('gml', 'SANITIZED'),
                            'Jarrett L' : ('jml', 'SANITIZED'),
                            'Kimberly V':
                                ('kvp', 'SANITIZED')
                            }

        self.ui.file_enter.clicked.connect(self.file_clicked)
        self.ui.row_enter.clicked.connect(self.enter_clicked)
        self.ui.copy_info.clicked.connect(self.person_info_clicked)
        self.ui.copy_msg.clicked.connect(self.person_msg_clicked)
        self.ui.found.clicked.connect(self.found_clicked)
        self.ui.notfound.clicked.connect(self.not_found_clicked)
        self.ui.next_person.clicked.connect(self.next_clicked)
        self.ui.template_combo.currentIndexChanged.connect(self.get_person_selected)
        self.ui.person_combo.currentIndexChanged.connect(self.get_person_selected)
        self.ui.loading_label.hide()


    def file_clicked(self):
        path = self.ui.filename_box.toPlainText()
        template = self.get_template_selected()

        self.LI = LinkedIn(path, template)
        self.LI.row_number = 1
        self.LI.generate_pdtable()
        self.persons = self.LI.get_persons()

        self.ui.filename_box.setPlainText(path)
        self.ui.loading_label.show()


    def enter_clicked(self):
        while True:
            try:
                row = int(self.ui.row_box.toPlainText())
                self.LI.row_number = row
                break
            except:
                self.ui.row_box.setPlainText('Invalid number: try again')

        self.ui.row_box.setPlainText(str(self.LI.row_number))
        self.ui.person_counter.setText(str(self.LI.row_number) + ' / ' + str(self.LI.max_rows + 1))

        person = self.persons[self.LI.row_number - 2]

        person_name, person_company, person_type, person_role = person[0], person[1], person[2], person[3]
        self.ui.person_info.setPlainText(person_name + '\n' + person_company + '\n' + person_type + '\n' + person_role)
        self.ui.person_msg.setPlainText(str(self.generate_msg(person)))


    def found_clicked(self):
        self.LI.write_found()
        self.next_clicked()


    def not_found_clicked(self):
        self.LI.write_not_found()
        self.next_clicked()


    def person_info_clicked(self):
        text = self.ui.person_info.toPlainText()
        name_and_company = text.split('\n')[:2]
        text = name_and_company[0] + ' ' + name_and_company[1]
        text = text.strip(',')
        subprocess.run(['clip.exe'], input=text.strip().encode('utf-16'), check=True)


    def person_msg_clicked(self):
        text = self.ui.person_msg.toPlainText()
        subprocess.run(['clip.exe'], input=text.strip().encode('utf-16'), check=True)


    def next_clicked(self):
        self.LI.row_number += 1
        self.set_window()


    def get_person_selected(self):
        return self.ui.person_combo.currentText()


    def get_template_selected(self):
        return self.ui.template_combo.currentText()


    def set_window(self):
        self.ui.row_box.setPlainText(str(self.LI.row_number))
        self.ui.person_counter.setText(str(self.LI.row_number) + ' / ' + str(self.LI.max_rows + 1))

        person = self.persons[self.LI.row_number - 2]

        if self.get_template_selected() == 'Default':
            person_name, person_company, person_type, person_role = person[0], person[1], person[2], person[3]
            self.ui.person_info.setPlainText(person_name + '\n' + person_company + '\n' + person_type + '\n' + person_role)
        else:
            person_name, person_company = person[0], person[1]
            self.ui.person_info.setPlainText(person_name + '\n' + person_company)
        self.ui.person_msg.setPlainText(str(self.generate_msg(person)))


    def generate_msg(self, person):
        if self.get_template_selected() == 'Default':
            name, type, role = person[0], person[2], person[3]
            name = name.split()
            first, last = name[0], name[1]
            employee = self.get_person_selected()

            if 'Account' in type or 'Account' in role:
                return 'Dear {first} {last},\n\n' \
                       'I am expanding my contact base of highly regarded accounting professionals ' \
                       'with a practice focus in M&A/Corporate Finance as a resource for our firm’s clients.\n\n' \
                       'Regards,\n' \
                       '{name}\n' \
                       'Global Capital Markets Inc.\n' \
                       '{phone}\n' \
                       '{email}@email.com'.format(first=first, last=last, name=employee,
                                                                        phone=self.person_dict[employee][1], email=self.person_dict[employee][0])


            elif 'Consult' in type or 'Consult' in role:
                return 'Dear {first} {last},\n\n' \
                       'I am expanding my contact base of well-established business consultants particularly ' \
                       'with experience/interest in M&A/Corporate Finance as a resource for our firm’s clients.\n\n' \
                       'Regards,\n' \
                       '{name}\n' \
                       'Global Capital Markets Inc.\n' \
                       '{phone}\n' \
                       '{email}@email.com'.format(first=first, last=last,
                                                                 name=employee,
                                                                 phone=self.person_dict[employee][1],
                                                                 email=self.person_dict[employee][0])


            elif ('Executive' or 'Director') in type or ('Executive' or 'Director') in role:
                return 'Dear {first} {last},\n\n' \
                       'I am expanding my contact base of well-established business executives particularly ' \
                       'with experience/interest in M&A/Corporate Finance as a resource for our firm’s clients.\n\n' \
                       'Regards,\n' \
                       '{name}\n' \
                       'Global Capital Markets Inc.\n' \
                       '{phone}\n' \
                       '{email}@email.com'.format(first=first, last=last,
                                                                 name=employee,
                                                                 phone=self.person_dict[employee][1],
                                                                 email=self.person_dict[employee][0])


            elif ('Law' or 'Attorney') in type or ('Law' or 'Attorney') in role:
                return 'Dear {first} {last},\n\n' \
                       'I am expanding my contact base of well-established M&A/Corporate Finance attorneys ' \
                       'as a resource for our firm’s clients.\n\n' \
                       'Regards,\n' \
                       '{name}\n' \
                       'Global Capital Markets Inc.\n' \
                       '{phone}\n' \
                       '{email}@email.com'.format(first=first, last=last,
                                                                 name=employee,
                                                                 phone=self.person_dict[employee][1],
                                                                 email=self.person_dict[employee][0])


            else:
                return 'Dear {first} {last},\n\n' \
                       'I am expanding my contact base of well-established _____________ particularly' \
                       'with experience/interest in M&A/Corporate Finance as a resource for our firm’s clients.\n\n' \
                       'Regards,\n' \
                       '{name}\n' \
                       'Global Capital Markets Inc.\n' \
                       '{phone}\n' \
                       '{email}@email.com'.format(first=first, last=last,
                                                                 name=employee,
                                                                 phone=self.person_dict[employee][1],
                                                                 email=self.person_dict[employee][0])


        elif self.get_template_selected() == 'Law Firms':
            name = person[0]
            name = name.split()
            first, last = name[0], name[1]
            employee = self.get_person_selected()
            return 'Dear {first} {last},\n\n' \
                   'I am expanding my contact base of highly regarded M&A/Corporate Finance attorneys ' \
                   'as a resource for our firm’s clients.\n\n' \
                   'Regards,\n' \
                   '{name}\n' \
                   'Global Capital Markets Inc.\n' \
                   '{phone}\n' \
                   '{email}@email.com'.format(first=first, last=last, name=employee,
                                                             phone=self.person_dict[employee][1],
                                                             email=self.person_dict[employee][0])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.setWindowTitle('GCM LinkedIn Connector')
    window.setWindowIcon(QtGui.QIcon('thumbnail_icon_green.png'))
    window.show()
    sys.exit(app.exec_())
    window = MainWindow()
    app.exec_()
    self.LI.table.close()