#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
License:            Creative Commons Attribution 4.0 International (CC BY 4.0)
                    http://creativecommons.org/licenses/by/4.0/

PURPOSE
------------------------------------------------------------------------------
Provide a pyqt application for the main pymdwizard application


SCRIPT DEPENDENCIES
------------------------------------------------------------------------------
    None


U.S. GEOLOGICAL SURVEY DISCLAIMER
------------------------------------------------------------------------------
Any use of trade, product or firm names is for descriptive purposes only and
does not imply endorsement by the U.S. Geological Survey.

Although this information product, for the most part, is in the public domain,
it also contains copyrighted material as noted in the text. Permission to
reproduce copyrighted items for other than personal use must be secured from
the copyright owner.

Although these data have been processed successfully on a computer system at
the U.S. Geological Survey, no warranty, expressed or implied is made
regarding the display or utility of the data on any other system, or for
general or scientific purposes, nor shall the act of distribution constitute
any such warranty. The U.S. Geological Survey shall not be held liable for
improper or incorrect use of the data described and/or contained herein.

Although this program has been used by the U.S. Geological Survey (USGS), no
warranty, expressed or implied, is made by the USGS or the U.S. Government as
to the accuracy and functioning of the program and related program material
nor shall the fact of distribution constitute any such warranty, and no
responsibility is assumed by the USGS in connection therewith.
------------------------------------------------------------------------------
"""
import sys, os

from lxml import etree


from PyQt5.QtWidgets import QMainWindow, QApplication, QSplashScreen, QMessageBox, QAction
from PyQt5.QtWidgets import QWidget, QLineEdit, QSizePolicy, QTableView
from PyQt5.QtWidgets import QStyleOptionHeader, QHeaderView, QStyle, QFileDialog
from PyQt5.QtCore import QAbstractItemModel, QModelIndex, QSize, QRect, QPoint, QFile, QTextStream, QFileInfo
from PyQt5.QtCore import Qt, QMimeData, QObject, QTimeLine, QSettings
from PyQt5.QtGui import QPainter, QFont, QFontMetrics, QPalette, QBrush, QColor, QPixmap, QDrag


from pymdwizard.gui.ui_files import UI_MainWindow
from pymdwizard.gui.MetadataRoot import MetadataRoot
from pymdwizard.core import xml_utils


class PyMdWizardMainForm(QMainWindow):

    max_recent_files = 5

    def __init__(self, parent=None):
        # QtGui.QMainWindow.__init__(self, parent)
        super(self.__class__, self).__init__()

        self.recent_file_actions = []

        self.build_ui()
        self.connect_events()

    def build_ui(self):
        """
        Build and modify this widget's GUI

        Returns
        -------
        None
        """
        self.ui = UI_MainWindow.Ui_MainWindow()
        self.ui.setupUi(self)

        self.metadata_root = MetadataRoot()
        self.ui.centralwidget.setLayout(self.metadata_root.layout())

        for i in range(PyMdWizardMainForm.max_recent_files):
            self.recent_file_actions.append(
                QAction(self, visible=False,
                        triggered=self.open_recent_file))
            self.ui.menuRecent_Files.addAction(self.recent_file_actions[i])
        self.update_recent_file_actions()

    def connect_events(self):
        """
        Connect the appropriate GUI components with the corresponding functions

        Returns
        -------
        None
        """
        self.ui.actionOpen.triggered.connect(self.open_file)
        self.ui.actionSave.triggered.connect(self.save_file)
        self.ui.actionSave_as.triggered.connect(self.save_as)

    def open_recent_file(self):
        """
        handles the opening of a recent file selection
        Returns
        -------
        None
        """
        action = self.sender()
        if action:
            self.load_file(action.data())

    def open_file(self):
        """
        Browse to a file and load it if it is acceptable

        Returns
        -------
        None
        """

        settings = QSettings('USGS', 'pymdwizard')
        recent_files = settings.value('recentFileList', [])
        if recent_files:
            dname, fname = os.path.split(recent_files[0])
        else:
            fname, dname = "", ""

        fname = QFileDialog.getOpenFileName(self, fname, dname)
        if fname[0]:
            self.load_file(fname[0])
            self.update_recent_file_actions()

    def load_file(self, fname):
        """
        load a file's content into the application.

        Parameters
        ----------
        fname : str
                full file path and name of the file to load
        Returns
        -------
        None
        """
        file = QFile(fname)
        if not file.open(QFile.ReadWrite | QFile.Text):
            msg = "Cannot open file %s:\n%s." % (fname, file.errorString())
            QMessageBox.warning(self, "Recent Files", msg)

            return
        file.close()

        try:
            new_record = etree.parse(fname)
            self.metadata_root._from_xml(new_record)

            self.set_current_file(fname)
            self.statusBar().showMessage("File loaded", 2000)
        except:
            msg = "Cannot open file %s:\n%s." % (fname, file.errorString())
            QMessageBox.warning(self, "Recent Files", msg)

    def save_as(self):
        """
        Navigate to a new or existing file and save the current document
        into this file.

        Returns
        -------
        None
        """
        settings = QSettings('USGS', 'pymdwizard')
        recent_files = settings.value('recentFileList', [])
        if recent_files:
            dname, fname = os.path.split(recent_files[0])
        else:
            fname, dname = "", ""

        fname = QFileDialog.getSaveFileName(self, fname, dname)
        if fname[0]:
            self.set_current_file(fname[0])
            self.update_recent_file_actions()
            self.save_file()

    def save_file(self, e=None):
        file = QFile(self.cur_fname)
        if not file.open(QFile.ReadWrite | QFile.Text):
            msg = "Cannot write file %s:\n%s.".format(self.cur_fname,
                                                      file.errorString())
            QMessageBox.warning(self, "Metadata Wizard", msg)
            return

        out_str = QTextStream(file)
        QApplication.setOverrideCursor(Qt.WaitCursor)
        out_str << xml_utils.node_to_string(self.metadata_root._to_xml())
        QApplication.restoreOverrideCursor()

        self.set_current_file(self.cur_fname)
        self.statusBar().showMessage("File saved", 2000)

    def set_current_file(self, fname):
        self.cur_fname = fname
        if self.cur_fname:
            title = "%s - Recent Files" % self.stripped_name(self.cur_fname)
            self.setWindowTitle(title)
        else:
            self.setWindowTitle("Metadata Wizard")

        settings = QSettings('USGS', 'pymdwizard')
        files = settings.value('recentFileList', [])

        try:
            files.remove(fname)
        except ValueError:
            pass

        files.insert(0, fname)
        del files[PyMdWizardMainForm.max_recent_files:]

        settings.setValue('recentFileList', files)

        for widget in QApplication.topLevelWidgets():
            if isinstance(widget, PyMdWizardMainForm):
                widget.update_recent_file_actions()

    def update_recent_file_actions(self):
        settings = QSettings('USGS', 'pymdwizard')
        files = settings.value('recentFileList', [])

        num_recent_files = min(len(files), PyMdWizardMainForm.max_recent_files)

        for i in range(num_recent_files):
            text = "&%d %s" % (i + 1, self.stripped_name(files[i]))
            self.recent_file_actions[i].setText(text)
            self.recent_file_actions[i].setData(files[i])
            self.recent_file_actions[i].setVisible(True)

        for j in range(num_recent_files, PyMdWizardMainForm.max_recent_files):
            self.recent_file_actions[j].setVisible(False)

    def stripped_name(self, full_fname):
        return QFileInfo(full_fname).fileName()


def main():
    app = QApplication(sys.argv)

    mdwiz = PyMdWizardMainForm()
    mdwiz.show()
    app.exec_()


if __name__ == '__main__':
    main()