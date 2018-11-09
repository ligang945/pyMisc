#!/usr/bin/python

import os
import time

def sleep():
    time.sleep(300)
    
def start_merge():
    os.system("./start_merge.sh")
    
def stop_merge():
    os.system("./stop_merge.sh")
    
def prepare_data(protocol_name):
    os.system("rm -r ReadyData/*")
    if protocol_name == 'bssap+ranap+bicc+h248':
        os.system("ln -s /DX80/dp10_data/guangzhou_yd_\[ip_14_bsmap_ranap_dtap_gsmmap_tpdu\]\[ip_24_bicc_h248\]\[e1_2m_24_tcap_gsmmap_cap_bssmap_ranap\]\[e1_2m_btsm_dtap_rpdu\]/A_data/* ReadyData/")
    if protocol_name == 'map+cap+isup':
        os.system("ln -s `/DX80/dp10_data/benchmark/map_cap_isup_hungary_ip/* ReadyData/")
    if protocol_name == 'bssap':
        os.system("ln -s /DX80/dp10_data/benchmark/pure_bssap_guangzhou_ip/* ReadyData/")
    elif protocol_name == 'ranap':
        os.system("ln -s /DX80/dp10_data/benchmark/pure_ranap_guangzhou_ip/* ReadyData/")
    elif protocol_name == 'bicc':
        os.system("ln -s /DX80/dp10_data/benchmark/pure_bicc_guangzhou_ip/* ReadyData/")
    elif protocol_name == 'h248':
        os.system("ln -s /DX80/dp10_data/benchmark/pure_h248_guangzhou_ip/* ReadyData/")
    elif protocol_name == 'gsm-map':
        os.system("ln -s /DX80/dp10_data/benchmark/pure_gsm_map_xili_E1/* ReadyData/")
    elif protocol_name == 'gsm-cap':
        os.system("ln -s /DX80/dp10_data/benchmark/pure_gsm_cap_xili_E1/* ReadyData/")
    elif protocol_name == 'tup':
        os.system("ln -s /DX80/dp10_data/benchmark/pure_tup_E1_2M/* ReadyData/")
    elif protocol_name == 'isup':
        os.system("ln -s /DX80/dp10_data/benchmark/pure_isup_chongqing_ip/* ReadyData/")
    elif protocol_name == 'diameter':
        os.system("ln -s /DX80/dp10_data/benchmark/pure_diameter/* ReadyData/")
    elif protocol_name == 'megaco':
        os.system("ln -s /DX80/dp10_data/benchmark/pure_megaco_hungary_ip/* ReadyData/")
    elif protocol_name == 's1ap':
        os.system("ln -s /DX80/dp10_data/benchmark/pure_s1ap/* ReadyData/")
    elif protocol_name == 'gtpv2':
        os.system("ln -s /DX80/dp10_data/benchmark/pure_gtpv2/* ReadyData/")

def replace_in_config_file(old_str, new_str):
    file_name = '../static_config/ini/protocolstate.ini'
    str = open(file_name, 'r').read().replace(old_str, new_str)
    open(file_name, 'w').write(str)    
    
def prepare_config(protocol_name):
    replace_in_config_file('= 1', '= 0')
    if protocol_name == 'bssap+ranap+bicc+h248':
        replace_in_config_file('BSSAP_Enable = 0', 'BSSAP_Enable = 1')
        replace_in_config_file('RANAP_Enable = 0', 'RANAP_Enable = 1')
        replace_in_config_file('BICC_Enable = 0', 'BICC_Enable = 1')
        replace_in_config_file('H248_Enable = 0', 'H248_Enable = 1')
    if protocol_name == 'map+cap+isup':
        replace_in_config_file('GSM_MAP_Enable = 0', 'GSM_MAP_Enable = 1')
        replace_in_config_file('GSM_CAP_Enable = 0', 'GSM_CAP_Enable = 1')
        replace_in_config_file('ISUP_Enable = 0', 'ISUP_Enable = 1')
    if protocol_name == 'bssap':
        replace_in_config_file('BSSAP_Enable = 0', 'BSSAP_Enable = 1')
    elif protocol_name == 'ranap':
        replace_in_config_file('RANAP_Enable = 0', 'RANAP_Enable = 1')
    elif protocol_name == 'bicc':
        replace_in_config_file('BICC_Enable = 0', 'BICC_Enable = 1')
    elif protocol_name == 'h248':
        replace_in_config_file('H248_Enable = 0', 'H248_Enable = 1')
    elif protocol_name == 'gsm-map':
        replace_in_config_file('GSM_MAP_Enable = 0', 'GSM_MAP_Enable = 1')
    elif protocol_name == 'gsm-cap':
        replace_in_config_file('GSM_CAP_Enable = 0', 'GSM_CAP_Enable = 1')
    elif protocol_name == 'tup':
        replace_in_config_file('TUP_Enable = 0', 'TUP_Enable = 1')
    elif protocol_name == 'isup':
        replace_in_config_file('ISUP_Enable = 0', 'ISUP_Enable = 1')
    elif protocol_name == 'diameter':
        replace_in_config_file('DIAMETER_Enable = 0', 'DIAMETER_Enable = 1')
    elif protocol_name == 'megaco':
        replace_in_config_file('MEGACO_Enable = 0', 'MEGACO_Enable = 1')
    elif protocol_name == 's1ap':
        replace_in_config_file('S1AP_Enable = 0', 'S1AP_Enable = 1')
    elif protocol_name == 'gtpv2':
        replace_in_config_file('GTPv2_Enable = 0', 'GTPv2_Enable = 1')

def test(protocol_name):
    print "----------- test %s -----------" % protocol_name
    stop_merge()
    prepare_data(protocol_name)
    prepare_config(protocol_name)
    start_merge()
    sleep()

def main():
    print "========== test begin ! =========="
    test("bssap+ranap+bicc+h248")
    # test("map+cap+isup")
    # test("bssap")
    # test("ranap")
    # test("bicc")
    # test("h248")
    # test("gsm-map")
    # test("gsm-cap")
    # test("tup")
    # test("isup")
    # test("diameter")
    # test("megaco")
    # test("s1ap")
    # test("gtpv2")
    print "========== test complete ! =========="

if __name__ == '__main__':
    main()
