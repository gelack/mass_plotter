# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 22:04:03 2017

@author: GLackner
"""
import os
import emzed
import plot_tools as pl




def gui_get_TIC_params():
    DialogBuilder = emzed.gui.DialogBuilder
    format_choice = ['pdf', 'png', 'svg']
    params = DialogBuilder('XIC parameters')\
    .addFileOpen('Select peakmap',formats=['mzXML', 'mzML'])\
    .addDirectory('Please choose result directory')\
    .addChoice("Format", format_choice, default=0,\
                            help='File format for spectra plot. Possible formats: pdf, png, svg')\
    .addFloat('rtmin', default=0.0, help='lower boundary of retention time')\
    .addFloat("rtmax", default=0.0, help="upper boundary of retention time")\
    .show()
    peakmap_path, results_directory, format_select, rtmin, rtmax = params
    rtmin = rtmin*60 #compute seconds
    rtmax = rtmax*60
    if (rtmin, rtmax) == (0.0,0.0):
        (rtmin, rtmax) = (None, None)
    format_ = format_choice[format_select]
    params = peakmap_path, results_directory, format_, rtmin, rtmax
    return params

def gui_get_XIC_params():
    DialogBuilder = emzed.gui.DialogBuilder
    format_choice = ['pdf', 'png', 'svg']
    params = DialogBuilder('XIC parameters')\
    .addFileOpen('Select peakmap',formats=['mzXML', 'mzML'])\
    .addDirectory('Please choose result directory')\
    .addChoice("Format", format_choice, default=0,\
                            help='File format for spectra plot. Possible formats: pdf, png, svg')\
    .addFloat('mzmin', help='lower boundary of mz')\
    .addFloat("mzmax", help="upper boundary of mz")\
    .addFloat('rtmin', default=0.0, help='lower boundary of retention time')\
    .addFloat("rtmax", default=0.0, help="upper boundary of retention time")\
    .show()
    peakmap_path, results_directory, format_select, mzmin, mzmax, rtmin, rtmax = params
    rtmin = rtmin*60 #compute seconds
    rtmax = rtmax*60
    if (rtmin, rtmax) == (0.0,0.0):
        (rtmin, rtmax) = (None, None)

    format_ = format_choice[format_select]
    
    params = peakmap_path, results_directory, format_, mzmin, mzmax, rtmin, rtmax
    return params

def gui_get_plot_spectrum_params():
    format_choice = ['pdf', 'png', 'svg']
  
    params = emzed.gui.DialogBuilder('Plot parameters')\
    .addFileOpen('select peakmap',formats=['mzXML', 'mzML'])\
    .addText("Scan numbers", help="Scan numbers of spectra to print, separated by line breaks")\
    .addInt("Number of decimals for spectrum plot", default=2, help="Number of decimals of mz value labels in spectrum plot")\
    .addFloat("Relative intesity threshold for peak labels", default = 0.05,\
                            help="Relative intensity a peak must reach to get labeled")\
    .addChoice("Formate", format_choice, default=0,\
                            help='File format for spectra plot. Possible formats: pdf, png, svg')\
    .addDirectory('Please choose result directory')\
    .show()
    path_to_pm, scan_numbers_txt, decimals, rel_int, format_select, path = params
    format_ = format_choice[format_select]
    scan_numbers_list = get_int_from_text(scan_numbers_txt)
    params = path_to_pm, scan_numbers_list, decimals, rel_int, format_, path
    return params

def gui_get_export_spectrum_params():
    format_choice = ['mgf']
    params = emzed.gui.DialogBuilder('Plot parameters')\
    .addFileOpen('select peakmap',formats=['mzXML', 'mzML'])\
    .addText("Scan numbers", help="Scan number of spectrum to print, separated by line breaks")\
    .addInt("Number of decimals", default=6, help="Number of decimals of mz values")\
    .addChoice("Formate", format_choice, default=0,\
                           help='File format for spectra plot. Possible formats: mgf')\
    .addDirectory('Please choose result directory')\
    .show()
    path_to_pm, scan_numbers_txt, decimals, format_select, path = params
    format_ = format_choice[format_select]
    scan_numbers_list = get_int_from_text(scan_numbers_txt)
    params = path_to_pm, scan_numbers_list, decimals, format_, path
    return params

def get_int_from_text(text):
        '''return each line represents one integer'''
        int_list_string =  text.splitlines()
        int_list = []
        for item in int_list_string:
            try: 
                int_ = int(item)
                int_list.append(int_)
            except ValueError:
                print "Please provide a number as input"
        return int_list



def plot_tic(__):
    params = gui_get_TIC_params()
    peakmap_path, results_directory, format_, rtmin, rtmax = params
    pm = emzed.io.loadPeakMap(peakmap_path)
    pl.plot_xic(pm, results_directory, rtmin=rtmin, rtmax=rtmax, format_=format_)
    return
    
def plot_xic(__):
    params = gui_get_XIC_params()
    peakmap_path, results_directory, format_, mzmin, mzmax, rtmin, rtmax = params
    pm = emzed.io.loadPeakMap(peakmap_path)
    pl.plot_xic(pm, results_directory, mzmin=mzmin, mzmax=mzmax, rtmin=rtmin, rtmax=rtmax, format_=format_)

def plot_spectrum(__):
    params = gui_get_plot_spectrum_params()
    path_to_pm, scan_numbers_list, decimals, rel_int, format_, path = params
    pm = emzed.io.loadPeakMap(path_to_pm)
    print "Peakmap loaded"
    for scan_number in scan_numbers_list:
        print "Scan: %i" % scan_number
        pl.plot_scan(pm, scan_number, rel_int=rel_int, decimals=decimals, path=path, format_=format_)
    return
    
def export_spectrum(__):
    params = gui_get_export_spectrum_params()
    path_to_pm, scan_numbers_list, decimals, format_, path = params
    pm = emzed.io.loadPeakMap(path_to_pm)
    print "Peakmap loaded"
    for scan_number in scan_numbers_list:
        print "Scan: %i" % scan_number
        pl.export_scan(pm, scan_number, path, decimals=decimals,format_=format_)
    return
        
def main_workflow():
    emzed.gui.DialogBuilder('Please select a task...   ')\
    .addButton('Plot TIC', plot_tic)\
    .addButton('Plot XIC', plot_xic)\
    .addButton('Plot mass spectrum', plot_spectrum)\
    .addButton('Export mass spectrum as . mgf', export_spectrum)\
    .show()

if __name__=='__main__':
    main_workflow()



 
