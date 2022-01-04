"""
script to generate all plots

Instruction:
    edit the first section "user-specified settings" for 
"""
import numpy as np
from esmac_diags.plotting import *


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# user-specified settings
settings = {}

# set field campaign name. More settings on specific field campaigns are in next section
# HISCALE, ACEENA, CSET, SOCRATES, MAGIC, MARCUS
settings['campaign'] = 'MAGIC'

# set model names. 
settings['Model_List'] = ['E3SMv1']
# settings['Model_List'] = ['E3SMv1','EAMv1_CONUS_RRM']

# set line colors for each model. corresponding to the Model_List
settings['color_model'] = ['r','b','g']

# set field campaign IOPs. Only used for HISCALE and ACEENA. 
# IOP1/IOP2 
settings['IOP'] = 'IOP1'

########## set filepath for preprocessing. If you don't run preprocessing, ignore this part
# path of E3SM model data (h3) for preprocessing. same length of Model_List
# settings['E3SM_hourly_path'] = ['/global/cscratch1/sd/sqtang/EAGLES/E3SM_output/E3SMv1_hourly/']
#settings['E3SM_hourly_path'] = \
#    ['/global/cscratch1/sd/sqtang/EAGLES/E3SM_output/E3SMv1_hourly/', \
#     '/global/cscratch1/sd/sqtang/EAGLES/E3SM_output/E3SMv1_hourly/']
#settings['E3SM_hourly_filehead'] = ['E3SMv1','EAMv1_CONUS_RRM']
#############

# Please specify the path of your data and for figure output
settings['figpath'] = '/global/cscratch1/sd/sqtang/EAGLES/Aerosol_diag_pkg/figures/'
settings['datapath'] = '/global/cscratch1/sd/sqtang/EAGLES/Aerosol_diag_pkg/data/'


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def add_other_setting(settings):
    """
    add other settings for different field campaigns

    Parameters
    ----------
    settings : dictionary
        all setting variables

    Returns
    -------
    settings

    """
    figpath = settings['figpath']+settings['campaign']
    datapath = settings['datapath']+settings['campaign']
    
    # path of output figures
    settings['figpath_aircraft_timeseries'] = figpath+'/aircraft/timeseries/'
    settings['figpath_aircraft_statistics'] = figpath+'/aircraft/statistics/'
    settings['figpath_ship_timeseries'] = figpath+'/ship/timeseries/'
    settings['figpath_ship_statistics'] = figpath+'/ship/statistics/'
    settings['figpath_sfc_timeseries'] = figpath+'/surface/timeseries/'
    settings['figpath_sfc_statistics'] = figpath+'/surface/statistics/'
    settings['figpath_profile_timeseries'] = figpath+'/profile/timeseries/'
    
    # other settings for different field campaigns
    if settings['campaign']=='HISCALE':
        settings['site']='SGP'
        # lat/lon at SGP
        settings['lat0'] = 36.6059
        settings['lon0'] = 360-97.48792     # 0-360
        # bin of flight heights to calculate percentiles
        settings['height_bin'] = np.arange(300,4300,300)
        # time periods for IOPs. needed in preprocessing of surface data
        if settings['IOP']=='IOP1':
            settings['start_date']='2016-04-25'
            settings['end_date']='2016-05-29'
        elif settings['IOP']=='IOP2':
            settings['start_date']='2016-08-27'
            settings['end_date']='2016-09-22'
        #### observational data path. ######
        settings['merged_size_path'] = datapath+'/obs/aircraft/merged_bin/'
        settings['iwgpath'] = datapath+'/obs/aircraft/mei-iwg1/'
        settings['fimspath'] = datapath+'/obs/aircraft/wang-fims/'
        settings['pcasppath'] = datapath+'/obs/aircraft/tomlinson-pcasp/'
        settings['cvipath'] = datapath+'/obs/aircraft/pekour-cvi/'
        settings['cpcpath'] = datapath+'/obs/aircraft/mei-cpc/'
        settings['ccnpath'] = datapath+'/obs/aircraft/mei-ccn/'
        settings['amspath'] = datapath+'/obs/aircraft/shilling-ams/'
        settings['wcmpath'] = datapath+'/obs/aircraft/matthews-wcm/'
        # surface measurements
        settings['smps_pnnl_path'] = datapath+'/obs/surface/pnnl-smps/'
        settings['smps_bnl_path'] = datapath+'/obs/surface/bnl-smps/'
        settings['nanosmps_bnl_path'] = datapath+'/obs/surface/bnl-nanosmps/'
        settings['uhsassfcpath'] = datapath+'/obs/surface/arm-uhsas/'
        settings['cpcsfcpath'] = datapath+'/obs/surface/arm-cpc/'
        settings['cpcusfcpath'] = datapath+'/obs/surface/arm-cpcu/'
        settings['ccnsfcpath'] = datapath+'/obs/surface/arm-ccn/'
        settings['metpath'] = datapath+'/obs/surface/arm-met/'
        settings['acsmpath'] = datapath+'/obs/surface/arm_acsm/'
        # vertical profile measurements
        settings['armbepath'] = datapath+'/obs/profile/sgparmbecldrad/'
        # PBLH data needed for plot_flight_pdf_percentile_SeparatePBLH_hiscale.py only
        settings['pblhpath'] = datapath+'/obs/profile/arm-pblh/'
        settings['dlpath'] = datapath+'/obs/profile/dl-pblh/'
        #### pre-processed model data path ######
        settings['E3SM_sfc_path'] = datapath+'/model/surface/'
        settings['E3SM_aircraft_path'] = datapath+'/model/flighttrack/'
        settings['E3SM_profile_path'] = datapath+'/model/profile/'
        ########################
        
    elif settings['campaign']=='ACEENA':
        settings['site']='ENA'
        # lat/lon for ENA
        settings['lat0'] = 39.09527
        settings['lon0'] = 360-28.0339
        # bin of flight heights to calculate percentiles
        settings['height_bin'] = np.arange(100,4300,300)
        # time periods for IOPs. needed in preprocessing of surface data
        if settings['IOP']=='IOP1':
            settings['start_date']='2017-06-20'
            settings['end_date']='2017-07-20'
        elif settings['IOP']=='IOP2':
            settings['start_date']='2018-01-21'
            settings['end_date']='2018-02-19'
        #### observational data path. ######
        settings['merged_size_path']=datapath+'/obs/aircraft/merged_bin/'
        settings['iwgpath'] = datapath+'/obs/aircraft/IWG/'
        settings['cvipath'] = datapath+'/obs/aircraft/inletcvi/'
        settings['amspath'] = datapath+'/obs/aircraft/shilling-hrfams/'
        settings['fimspath'] = datapath+'/obs/aircraft/FIMS/'
        settings['pcasppath'] = datapath+'/obs/aircraft/pcasp_g1/'
        settings['opcpath'] = datapath+'/obs/aircraft/opciso/'
        settings['cpcpath'] = datapath+'/obs/aircraft/cpc_aaf/'
        settings['ccnpath'] = datapath+'/obs/aircraft/ccn_aaf/'
        settings['amspath'] = datapath+'/obs/aircraft/shilling-hrfams/'
        settings['wcmpath'] = datapath+'/obs/aircraft/wcm_ACEENA/'
        # surface measurements
        settings['uhsassfcpath'] = datapath+'/obs/surface/arm_uhsas/'
        settings['cpcsfcpath'] = datapath+'/obs/surface/arm_cpcf/'
        settings['cpcusfcpath'] = 'N/A'
        settings['ccnsfcpath'] = datapath+'/obs/surface/arm_aosccn1/'
        settings['metpath'] = datapath+'/obs/surface/arm_met/'
        settings['acsmpath'] = datapath+'/obs/surface/arm_acsm/'
        # vertical profile measurements
        settings['armbepath'] = datapath+'/obs/profile/enaarmbecldrad/'
        #### pre-processed model data path ######
        settings['E3SM_sfc_path'] = datapath+'/model/surface/'
        settings['E3SM_aircraft_path'] = datapath+'/model/flighttrack/'
        settings['E3SM_profile_path'] = datapath+'/model/profile/'
        #########
    elif settings['campaign']=='MAGIC':
        settings['site']='MAG'
        # bin of latitude to calculate ship track composite
        settings['latbin'] = np.arange(21.5,34,1)
        # reference lat/lon
        settings['lat0']=30.
        settings['lon0']=230.
        #### observational data path. ######
        settings['shipmetpath'] = datapath+'/obs/ship/raynolds-marmet/'
        settings['shipccnpath'] = datapath+'/obs/ship/magaosccn100M1.a1/'
        settings['shipcpcpath'] = datapath+'/obs/ship/magaoscpcfM1.a1/'
        settings['shipmwrpath'] = datapath+'/obs/ship/magmwrret1liljclouM1.s2/'
        settings['shipuhsaspath'] = datapath+'/obs/ship/magaosuhsasM1.a1/'
        #### pre-processed model data path ######    
        settings['E3SM_ship_path'] = datapath+'/model/shiptrack/'
        settings['E3SM_profile_path'] = datapath+'/model/profile/'
        ################
    elif settings['campaign']=='MARCUS':
        settings['site'] = 'MAR'
        # bin of latitude to calculate ship track composite
        settings['latbin'] = np.arange(-68.5,-42,1)
        # reference lat/lon
        settings['lat0'] = -40.
        settings['lon0'] = 120.
        #### observational data path. ######
        settings['shipmetpath'] = datapath+'/obs/ship/maraadmetX1.b1/'
        settings['shipccnpath'] = datapath+'/obs/ship/maraosccn1colavgM1.b1/'
        settings['shipcpcpath'] = datapath+'/obs/ship/maraoscpcf1mM1.b1/'
        settings['shipmwrpath'] = datapath+'/obs/ship/marmwrret1liljclouM1.s2/'
        settings['shipuhsaspath'] = datapath+'/obs/ship/maraosuhsasM1.a1/'
        #### pre-processed model data path ######    
        settings['E3SM_ship_path'] = datapath+'/model/shiptrack/'
        settings['E3SM_profile_path'] = datapath+'/model/profile/'
        ############
    elif settings['campaign']=='CSET':
        # bin of flight heights to calculate percentiles
        settings['height_bin'] = np.arange(200,8000,400)
        # bin of latitude to calculate composite percentiles, same as MAGIC
        settings['latbin'] = np.arange(22.5,39,1)
        # lat/lon at the airport
        settings['lat0'] = 38.5564
        settings['lon0'] = 360-121.3120
        #### observational data path. ######
        settings['RFpath'] = datapath+'/obs/aircraft/aircraft_lowrate/'
        settings['ccnpath'] = 'N/A'
        #### pre-processed model data path ###### 
        settings['E3SM_aircraft_path'] = datapath+'/model/flighttrack/'
        settings['E3SM_profile_path'] = datapath+'/model/profile/'
        ###############
    elif settings['campaign']=='SOCRATES':
        # bin of flight heights to calculate percentiles
        settings['height_bin'] = np.arange(200,8000,400)
        # bin of latitude to calculate composite percentiles
        settings['latbin'] = np.arange(-63.5,-42,1)
        # lat/lon at the airport
        settings['lat0'] = -42.8371
        settings['lon0'] = 147.5054
        #### observational data path. ######
        settings['RFpath'] = datapath+'/obs/aircraft/aircraft_lowrate/'
        settings['ccnpath'] = datapath+'/obs/aircraft/CCN/'
        #### pre-processed model data path ###### 
        settings['E3SM_aircraft_path'] = datapath+'/model/flighttrack/'
        settings['E3SM_profile_path'] = datapath+'/model/profile/'
        ################
    else:
        raise ValueError("does not recognize this campaign: "+settings['campaign'])
    return(settings)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def plot_all(settings):
    """
    include all plotting code. select for different field campaigns

    Parameters
    ----------
    settings : dictionary
        all setting variables for plotting.

    Returns
    -------
    None.

    """
    print('***** start plotting ********')
    if settings['campaign'] in ['HISCALE','ACEENA','CSET','SOCRATES']:
        print('********** plot flight data *****************')
        # flight information and timeseries
        plot_flight_track_height.run_plot(settings)
        plot_flight_timeseries_CN.run_plot(settings)
        contour_flight_timeseries_AerosolSize.run_plot(settings)
        plot_flight_timeseries_CCN.run_plot(settings)
        # vertical distribution
        plot_flight_percentile_z_CN.run_plot(settings)
        plot_flight_percentile_z_CCN.run_plot(settings)
        plot_flight_profile_z_CldFreq.run_plot(settings)
        plot_flight_profile_z_LWC.run_plot(settings)
        # mean statistics
        plot_flight_pdf_AerosolSize.run_plot(settings)
        calc_statistic_flight_CN.run_plot(settings)
        if settings['campaign'] in ['HISCALE','ACEENA']:
            plot_profile_cloud.run_plot(settings)
            plot_flight_timeseries_AerosolComposition.run_plot(settings)
            plot_flight_percentile_z_AerosolComposition.run_plot(settings)
        elif settings['campaign'] in ['CSET','SOCRATES']:
            plot_flight_percentile_lat_cldfreq.run_plot(settings)
            plot_flight_percentile_lat_CN.run_plot(settings)
            plot_flight_percentile_lat_CCN.run_plot(settings)
        if settings['campaign'] == 'HISCALE':
            plot_flight_pdf_percentile_SeparatePBLH_hiscale.run_plot(settings)
        if settings['campaign'] == 'ACEENA':
            plot_flight_pdf_percentile_SeparateCloud_aceena.run_plot(settings)
            
    if settings['campaign'] in ['HISCALE','ACEENA']:
        print('*********** plot surface data ***************')
        # time series
        plot_sfc_timeseries_CN.run_plot(settings)
        plot_sfc_timeseries_CCN.run_plot(settings)
        plot_sfc_timeseries_AerosolComposition.run_plot(settings)
        contour_sfc_timeseries_AerosolSize.run_plot(settings)
        # diurnal cycle
        plot_sfc_diurnalcycle_CN.run_plot(settings)
        plot_sfc_diurnalcycle_CCN.run_plot(settings)
        plot_sfc_diurnalcycle_AerosolComposition.run_plot(settings)
        contour_sfc_diurnalcycle_AerosolSize.run_plot(settings)
        # mean statistics
        plot_sfc_pdf_AerosolSize.run_plot(settings)
        plot_sfc_pie_AerosolComposition.run_plot(settings)
        calc_statistic_sfc_CN.run_plot(settings)
            
    if settings['campaign'] in ['MAGIC','MARCUS']:
        print('*********** plot ship data ***************')
        # time series
        plot_ship_timeseries_met.run_plot(settings)
        plot_ship_timeseries_CN.run_plot(settings)
        plot_ship_timeseries_CCN.run_plot(settings)
        # statistics
        plot_ship_percentile_lat_met.run_plot(settings)
        plot_ship_percentile_lat_CN.run_plot(settings)
        plot_ship_percentile_lat_CCN.run_plot(settings)
        plot_ship_percentile_lat_LWP.run_plot(settings)
        plot_ship_pdf_AerosolSize.run_plot(settings)
        contour_ship_timeseries_AerosolSize.run_plot(settings)
        calc_statistic_ship_CN.run_plot(settings)
            
    print('*********** end plotting **************')
    
#%% main
settings['campaign'] = 'MAGIC'
print('---------- plot for ' + settings['campaign'] + ' -----------')
plot_all(add_other_setting(settings))
settings['campaign'] = 'MARCUS'
print('---------- plot for ' + settings['campaign'] + ' -----------')
plot_all(add_other_setting(settings))
settings['campaign'] = 'CSET'
print('---------- plot for ' + settings['campaign'] + ' -----------')
plot_all(add_other_setting(settings))
settings['campaign'] = 'SOCRATES'
print('---------- plot for ' + settings['campaign'] + ' -----------')
plot_all(add_other_setting(settings))
settings['campaign'] = 'ACEENA'
settings['IOP'] = 'IOP1'
print('---------- plot for ' + settings['campaign'] + ' IOP1 -----------')
plot_all(add_other_setting(settings))
settings['IOP'] = 'IOP2'
print('---------- plot for ' + settings['campaign'] + ' IOP2 -----------')
plot_all(add_other_setting(settings))
settings['campaign'] = 'HISCALE'
settings['Model_List'] = ['E3SMv1','EAMv1_CONUS_RRM']
print('---------- plot for ' + settings['campaign'] + ' IOP2 -----------')
plot_all(add_other_setting(settings))
settings['IOP'] = 'IOP1'
print('---------- plot for ' + settings['campaign'] + ' IOP1 -----------')
plot_all(add_other_setting(settings))
