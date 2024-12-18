import sqlite3
import os

telemetry_data = [
    ('psarj', '0', '0', 'S0000004', 0),
    ('ssarj', '0', '0', 'S0000003', 1),
    ('ptrrj', '0', '0', 'S0000002', 2),
    ('strrj', '0', '0', 'S0000001', 3),
    ('beta1b', '0', '0', 'S6000008', 4),
    ('beta1a', '0', '0', 'S4000007', 5),
    ('beta2b', '0', '0', 'P6000008', 6),
    ('beta2a', '0', '0', 'P4000007', 7),
    ('beta3b', '0', '0', 'S6000007', 8),
    ('beta3a', '0', '0', 'S4000008', 9),
    ('beta4b', '0', '0', 'P6000007', 10),
    ('beta4a', '0', '0', 'P4000008', 11),
    ('aos', '0', '0', 'AOS', 12),
    ('los', '0', '0', 'LOS', 13),
    ('sasa1_elevation', '0', '0', 'S1000005', 14),
    ('sgant_elevation', '0', '0', 'Z1000014', 15),
    ('crewlock_pres', '0', '0', 'AIRLOCK000049', 16),
    ('sgant_xel', '0', '0', 'Z1000015', 17),
    ('sasa1_azimuth', '0', '0', 'S1000004', 18),
    ('loopb_flowrate', '0', '0', 'P1000001', 19),
    ('loopb_pressure', '0', '0', 'P1000002', 20),
    ('loopb_temp', '0', '0', 'P1000003', 21),
    ('loopa_flowrate', '0', '0', 'S1000001', 22),
    ('loopa_pressure', '0', '0', 'S1000002', 23),
    ('loopa_temp', '0', '0', 'S1000003', 24),
    ('voltage_1a', '0', '0', 'S4000001', 25),
    ('voltage_1b', '0', '0', 'S6000004', 26),
    ('voltage_2a', '0', '0', 'P4000001', 27),
    ('voltage_2b', '0', '0', 'P6000004', 28),
    ('voltage_3a', '0', '0', 'S4000004', 29),
    ('voltage_3b', '0', '0', 'S6000001', 30),
    ('voltage_4a', '0', '0', 'P4000004', 31),
    ('voltage_4b', '0', '0', 'P6000001', 32),
    ('current_1a', '0', '0', 'S4000002', 33),
    ('current_1b', '0', '0', 'S6000005', 34),
    ('current_2a', '0', '0', 'P4000002', 35),
    ('current_2b', '0', '0', 'P6000005', 36),
    ('current_3a', '0', '0', 'S4000005', 37),
    ('current_3b', '0', '0', 'S6000002', 38),
    ('current_4a', '0', '0', 'P4000005', 39),
    ('current_4b', '0', '0', 'P6000002', 40),
    ('kuband_transmit', '0', '0', 'Z1000013', 41),
    ('ptrrj_mode', '0', '0', 'S0000006', 42),
    ('strrj_mode', '0', '0', 'S0000007', 43),
    ('psarj_mode', '0', '0', 'S0000008', 44),
    ('ssarj_mode', '0', '0', 'S0000009', 45),
    ('russian_mode', '0', '0', 'RUSSEG000001', 46),
    ('iss_mode', '0', '0', 'USLAB000086', 47),
    ('iss_mass', '0', '0', 'USLAB000039', 48),
    ('us_gnc_mode', '0', '0', 'USLAB000012', 49),
    ('sasa2_elevation', '0', '0', 'P1000005', 50),
    ('sasa2_azimuth', '0', '0', 'P1000004', 51),
    ('sasa2_status', '0', '0', 'P1000007', 52),
    ('sasa1_status', '0', '0', 'S1000009', 53),
    ('active_sasa', '0', '0', 'USLAB000092', 54),
    ('position_x', '0', '0', 'USLAB000032', 55),
    ('position_y', '0', '0', 'USLAB000033', 56),
    ('position_z', '0', '0', 'USLAB000034', 57),
    ('velocity_x', '0', '0', 'USLAB000035', 58),
    ('velocity_y', '0', '0', 'USLAB000036', 59),
    ('velocity_z', '0', '0', 'USLAB000037', 60),
    ('PSA_EMU1_VOLTS', '0', '0', 'AIRLOCK000001', 61),
    ('PSA_EMU1_AMPS', '0', '0', 'AIRLOCK000002', 62),
    ('PSA_EMU2_VOLTS', '0', '0', 'AIRLOCK000003', 63),
    ('PSA_EMU2_AMPS', '0', '0', 'AIRLOCK000004', 64),
    ('PSA_IRU_Utility_VOLTS', '0', '0', 'AIRLOCK000005', 65),
    ('PSA_IRU_Utility_AMPS', '0', '0', 'AIRLOCK000006', 66),
    ('UIA_EV_1_VOLTS', '0', '0', 'AIRLOCK000007', 67),
    ('UIA_EV_1_AMPS', '0', '0', 'AIRLOCK000008', 68),
    ('UIA_EV_2_VOLTS', '0', '0', 'AIRLOCK000009', 69),
    ('UIA_EV_2_AMPS', '0', '0', 'AIRLOCK000010', 70),
    ('RPCM_AL1A4A_A_RPC_01_Depress_Pump_On_Off_Stat', '0', '0', 'AIRLOCK000047', 71),
    ('Airlock_Depress_Pump_Power_Switch', '0', '0', 'AIRLOCK000048', 72),
    ('Airlock_O2_Hi_P_Supply_Vlv_Actual_Posn', '0', '0', 'AIRLOCK000050', 73),
    ('Airlock_O2_Lo_P_Supply_Vlv_Actual_Posn', '0', '0', 'AIRLOCK000051', 74),
    ('Airlock_N2_Supply_Vlv_Actual_Posn', '0', '0', 'AIRLOCK000052', 75),
    ('Airlock_CCAA_State', '0', '0', 'AIRLOCK000053', 76),
    ('Airlock_PCA_Cabin_Pressure', '0', '0', 'AIRLOCK000054', 77),
    ('Airlock_O2_Hi_P_Supply_Pressure', '0', '0', 'AIRLOCK000055', 78),
    ('Airlock_O2_Lo_P_Supply_Pressure', '0', '0', 'AIRLOCK000056', 79),
    ('Airlock_N2_Supply_Pressure', '0', '0', 'AIRLOCK000057', 80),
    ('Node2_MTL_PPA_Avg_Accum_Qty', '0', '0', 'NODE2000001', 81),
    ('Node2_LTL_PPA_Avg_Accum_Qty', '0', '0', 'NODE2000002', 82),
    ('Node_2_CCAA_State', '0', '0', 'NODE2000003', 83),
    ('Node2_LTL_TWMV_Out_Temp', '0', '0', 'NODE2000006', 84),
    ('Node2_MTL_TWMV_Out_Temp', '0', '0', 'NODE2000007', 85),
    ('Node_3_MCA_ppO2', '0', '0', 'NODE3000001', 86),
    ('Node_3_MCA_ppN2', '0', '0', 'NODE3000002', 87),
    ('Node_3_MCA_ppCO2', '0', '0', 'NODE3000003', 88),
    ('Node_3_UPA_Current_State', '0', '0', 'NODE3000004', 89),
    ('Node_3_UPA_WSTA_Qty_Ctrl_Pct', '0', '0', 'NODE3000005', 90),
    ('Node_3_WPA_Process_Cmd_Status', '0', '0', 'NODE3000006', 91),
    ('Node_3_WPA_Process_Step', '0', '0', 'NODE3000007', 92),
    ('Node_3_WPA_Waste_Water_Qty_Ctrl', '0', '0', 'NODE3000008', 93),
    ('Node_3_WPA_Water_Storage_Qty_Ctrl', '0', '0', 'NODE3000009', 94),
    ('Node_3_OGA_Process_Cmd_Status', '0', '0', 'NODE3000010', 95),
    ('Node_3_OGA_O2_Production_Rate', '0', '0', 'NODE3000011', 96),
    ('Node3_MTL_TWMV_Out_Temp', '0', '0', 'NODE3000012', 97),
    ('Node3_LTL_TWMV_Out_Temp', '0', '0', 'NODE3000013', 98),
    ('Node3_MTL_PPA_Avg_Accum_Qty', '0', '0', 'NODE3000017', 99),
    ('Node_3_CCAA_State', '0', '0', 'NODE3000018', 100),
    ('Node3_LTL_PPA_Avg_Accum_Qty', '0', '0', 'NODE3000019', 101),
    ('DCSU_2A_PVCU_On_Off_V_Stat', '0', '0', 'P4000003', 102),
    ('DCSU_4A_PVCU_On_Off_V_Stat', '0', '0', 'P4000006', 103),
    ('DCSU_4B_RBI_6_Integ_I', '0', '0', 'P6000002', 104),
    ('DCSU_4B_PVCU_On_Off_V_Stat', '0', '0', 'P6000003', 105),
    ('DCSU_2B_PVCU_On_Off_V_Stat', '0', '0', 'P6000006', 106),
    ('RSMCS_SM_KURS1_On', '0', '0', 'RUSSEG000002', 107),
    ('RSMCS_SM_KURS2_On', '0', '0', 'RUSSEG000003', 108),
    ('SM_ECW_KURS_Fail', '0', '0', 'RUSSEG000004', 109),
    ('RSMCS_SM_KURS_Rng', '0', '0', 'RUSSEG000005', 110),
    ('RSMCS_SM_KURS_Vel', '0', '0', 'RUSSEG000006', 111),
    ('SM_KURS_P_Test_Mode_RS', '0', '0', 'RUSSEG000007', 112),
    ('SM_KURS_P_Capture_Signal_RS', '0', '0', 'RUSSEG000008', 113),
    ('SM_KURS_P_Target_Acquisition_Signal_RS', '0', '0', 'RUSSEG000009', 114),
    ('SM_KURS_P_Functional_Mode_Signal_RS', '0', '0', 'RUSSEG000010', 115),
    ('SM_KURS_P_In_Stand_by_Mode_RS', '0', '0', 'RUSSEG000011', 116),
    ('RSMCS_SM_Dock_Contact', '0', '0', 'RUSSEG000012', 117),
    ('RSMCS_SM_Forward_Port_Engaged', '0', '0', 'RUSSEG000013', 118),
    ('RSMCS_SM_Aft_Port_Engaged', '0', '0', 'RUSSEG000014', 119),
    ('RSMCS_SM_Nadir_Port_Engaged', '0', '0', 'RUSSEG000015', 120),
    ('RSMCS_SM_FGB_Nadir_Port_Engaged', '0', '0', 'RUSSEG000016', 121),
    ('RSMCS_SM_UDM_Nadir_Port_Engaged', '0', '0', 'RUSSEG000017', 122),
    ('RSMCS_MRM1_Port_Engaged', '0', '0', 'RUSSEG000018', 123),
    ('RSMCS_MRM2_Port_Engaged', '0', '0', 'RUSSEG000019', 124),
    ('RSMCS_SM_ETOV_Hooks_Closed', '0', '0', 'RUSSEG000020', 125),
    ('RSMCS_SM_Act_Att_Ref_Frame', '0', '0', 'RUSSEG000021', 126),
    ('RSMCS_SM_RS_Is_Master', '0', '0', 'RUSSEG000022', 127),
    ('RSMCS_SM_Ready_For_Indicator', '0', '0', 'RUSSEG000023', 128),
    ('RSProp_SM_Thrstr_Mode_Terminated', '0', '0', 'RUSSEG000024', 129),
    ('RSMCS_SM_SUDN_Mode', '0', '0', 'RUSSEG000025', 130),
    ('SARJ_Port_Commanded_Position', '0', '0', 'S0000005', 131),
    ('RPCM_S01A_C_RPC_01_Ext_1_MDM_On_Off_Stat', '0', '0', 'S0000010', 132),
    ('RPCM_S01A_C_RPC_16_S0_1_MDM_On_Off_Stat', '0', '0', 'S0000011', 133),
    ('RPCM_S02B_C_RPC_01_Ext_2_MDM_On_Off_Stat', '0', '0', 'S0000012', 134),
    ('RPCM_S02B_C_RPC_16_S0_2_MDM_On_Off_Stat', '0', '0', 'S0000013', 135),
    ('RPCM_S11A_C_RPC_03_STR_MDM_On_Off_Stat', '0', '0', 'S1000006', 136),
    ('RPCM_S11A_C_RPC_16_S1_1_MDM_On_Off_Stat', '0', '0', 'S1000007', 137),
    ('RPCM_S12B_B_RPC_05_S1_2_MDM_On_Off_Stat', '0', '0', 'S1000008', 138),
    ('DCSU_1A_PVCU_On_Off_V_Stat', '0', '0', 'S4000003', 139),
    ('DCSU_3A_PVCU_On_Off_V_Stat', '0', '0', 'S4000006', 140),
    ('DCSU_3B_PVCU_On_Off_V_Stat', '0', '0', 'S6000003', 141),
    ('DCSU_1B_PVCU_On_Off_V_Stat', '0', '0', 'S6000006', 142),
    ('Time of Occurrence', '0', '0', 'TIME_000001', 143),
    ('Year of Occurrence', '0', '0', 'TIME_000002', 144),
    ('USGNC_SEQ_CMG1_Online', '0', '0', 'USLAB000001', 145),
    ('USGNC_SEQ_CMG2_Online', '0', '0', 'USLAB000002', 146),
    ('USGNC_SEQ_CMG3_Online', '0', '0', 'USLAB000003', 147),
    ('USGNC_SEQ_CMG4_Online', '0', '0', 'USLAB000004', 148),
    ('USGNC_CA_Num_CMGs_Online', '0', '0', 'USLAB000005', 149),
    ('USGNC_CA_Unlim_Cntl_Trq_InBody_X', '0', '0', 'USLAB000006', 150),
    ('USGNC_CA_Unlim_Cntl_Trq_InBody_Y', '0', '0', 'USLAB000007', 151),
    ('USGNC_CA_Unlim_Cntl_Trq_InBody_Z', '0', '0', 'USLAB000008', 152),
    ('USGNC_CA_CMG_Mom_Act_Mag', '0', '0', 'USLAB000009', 153),
    ('USGNC_CA_CMG_Mom_Act_Cap_Pct', '0', '0', 'USLAB000010', 154),
    ('USGNC_CA_Desat_Request_Inh', '0', '0', 'USLAB000011', 155),
    ('USGNC_AD_Selected_Att_Source', '0', '0', 'USLAB000013', 156),
    ('USGNC_AD_Selected_Rate_Source', '0', '0', 'USLAB000014', 157),
    ('USGNC_SD_Selected_State_Source', '0', '0', 'USLAB000015', 158),
    ('USGNC_CA_Act_CCDB_Att_Cntl_Type', '0', '0', 'USLAB000016', 159),
    ('USGNC_CA_Act_CCDB_Att_Cntl_Ref_Frame', '0', '0', 'USLAB000017', 160),
    ('USGNC_PS_Pointing_LVLH_Att_Quatrn_0', '0', '0', 'USLAB000018', 161),
    ('USGNC_PS_Pointing_LVLH_Att_Quatrn_1', '0', '0', 'USLAB000019', 162),
    ('USGNC_PS_Pointing_LVLH_Att_Quatrn_2', '0', '0', 'USLAB000020', 163),
    ('USGNC_PS_Pointing_LVLH_Att_Quatrn_3', '0', '0', 'USLAB000021', 164),
    ('USGNC_CA_Att_Error_X', '0', '0', 'USLAB000022', 165),
    ('USGNC_CA_Att_Error_Y', '0', '0', 'USLAB000023', 166),
    ('USGNC_CA_Att_Error_Z', '0', '0', 'USLAB000024', 167),
    ('USGNC_PS_Pointing_Current_Inert_Rate_Vector_X', '0', '0', 'USLAB000025', 168),
    ('USGNC_PS_Pointing_Current_Inert_Rate_Vector_Y', '0', '0', 'USLAB000026', 169),
    ('USGNC_PS_Pointing_Current_Inert_Rate_Vector_Z', '0', '0', 'USLAB000027', 170),
    ('USGNC_CA_Act_CCDB_AttQuatrn_0_Cmd', '0', '0', 'USLAB000028', 171),
    ('USGNC_CA_Act_CCDB_AttQuatrn_1_Cmd', '0', '0', 'USLAB000029', 172),
    ('USGNC_CA_Act_CCDB_AttQuatrn_2_Cmd', '0', '0', 'USLAB000030', 173),
    ('USGNC_CA_Act_CCDB_AttQuatrn_3_Cmd', '0', '0', 'USLAB000031', 174),
    ('USGNC_CA_CMG_Mom_Act_Cap', '0', '0', 'USLAB000038', 175),
    ('USGNC_PS_Solar_Beta_Angle', '0', '0', 'USLAB000040', 176),
    ('USGNC_CA_Loss_Of_CMG_Att_Cntl_Latched_Caution', '0', '0', 'USLAB000041', 177),
    ('USGNC_CCS_Loss_of_ISS_Attitude_Control_Warning', '0', '0', 'USLAB000042', 178),
    ('USGNC_GPS1_Operational_Status', '0', '0', 'USLAB000043', 179),
    ('USGNC_GPS2_Operational_Status', '0', '0', 'USLAB000044', 180),
    ('USGNC_CMG1_SpinBrg_Temp1', '0', '0', 'USLAB000045', 181),
    ('USGNC_CMG2_SpinBrg_Temp1', '0', '0', 'USLAB000046', 182),
    ('USGNC_CMG3_SpinBrg_Temp1', '0', '0', 'USLAB000047', 183),
    ('USGNC_CMG4_SpinBrg_Temp1', '0', '0', 'USLAB000048', 184),
    ('USGNC_CMG1_SpinBrg_Temp2', '0', '0', 'USLAB000049', 185),
    ('USGNC_CMG2_SpinBrg_Temp2', '0', '0', 'USLAB000050', 186),
    ('USGNC_CMG3_SpinBrg_Temp2', '0', '0', 'USLAB000051', 187),
    ('USGNC_CMG4_SpinBrg_Temp2', '0', '0', 'USLAB000052', 188),
    ('LAB_MCA_ppO2', '0', '0', 'USLAB000053', 189),
    ('LAB_MCA_ppN2', '0', '0', 'USLAB000054', 190),
    ('LAB_MCA_ppCO2', '0', '0', 'USLAB000055', 191),
    ('LAB_LTL_PPA_Avg_Accum_Qty', '0', '0', 'USLAB000056', 192),
    ('LAB_MTL_PPA_Avg_Accum_Qty', '0', '0', 'USLAB000057', 193),
    ('LAB_PCA_Cabin_Pressure', '0', '0', 'USLAB000058', 194),
    ('LAB1P6_CCAA_In_T1', '0', '0', 'USLAB000059', 195),
    ('LAB_MTL_Regen_TWMV_Out_Temp', '0', '0', 'USLAB000060', 196),
    ('LAB_LTL_TWMV_Out_Temp', '0', '0', 'USLAB000061', 197),
    ('LAB_VRS_Vent_Vlv_Posn_Raw', '0', '0', 'USLAB000062', 198),
    ('LAB_VES_Vent_Vlv_Posn_Raw', '0', '0', 'USLAB000063', 199),
    ('LAB1P6_CCAA_State', '0', '0', 'USLAB000064', 200),
    ('LAB1S6_CCAA_State', '0', '0', 'USLAB000065', 201),
    ('RPCM_LAD11B_A_RPC_07_CC_1_MDM_On_Off_Stat', '0', '0', 'USLAB000066', 202),
    ('RPCM_LAD52B_A_RPC_03_CC_2_MDM_On_Off_Stat', '0', '0', 'USLAB000067', 203),
    ('RPCM_LA1A4A_E_RPC_01_CC_3_MDM_On_Off_Stat', '0', '0', 'USLAB000068', 204),
    ('RPCM_LAD11B_A_RPC_09_Int_1_MDM_On_Off_Stat', '0', '0', 'USLAB000069', 205),
    ('RPCM_LAD52B_A_RPC_04_Int_2_MDM_On_Off_Stat', '0', '0', 'USLAB000070', 206),
    ('RPCM_LAD11B_A_RPC_11_PL_1_MDM_On_Off_Stat', '0', '0', 'USLAB000071', 207),
    ('RPCM_LAD22B_A_RPC_01_PL_2_MDM_On_Off_Stat', '0', '0', 'USLAB000072', 208),
    ('RPCM_LA1B_B_RPC_14_GNC_1_MDM_On_Off_Stat', '0', '0', 'USLAB000073', 209),
    ('RPCM_LA2B_E_RPC_03_GNC_2_MDM_On_Off_Stat', '0', '0', 'USLAB000074', 210),
    ('RPCM_LAD11B_A_RPC_08_PMCU_1_MDM_On_Off_Stat', '0', '0', 'USLAB000075', 211),
    ('RPCM_LAD52B_A_RPC_01_PMCU_2_MDM_On_Off_Stat', '0', '0', 'USLAB000076', 212),
    ('RPCM_LA1B_B_RPC_09_LAB_1_MDM_On_Off_Stat', '0', '0', 'USLAB000077', 213),
    ('RPCM_LA2B_E_RPC_04_LAB_2_MDM_On_Off_Stat', '0', '0', 'USLAB000078', 214),
    ('RPCM_LA2B_E_RPC_13_LAB_3_MDM_On_Off_Stat', '0', '0', 'USLAB000079', 215),
    ('RPCM_LA1B_D_RPC_01_LAB_FSEGF_Sys_Pwr_1_On_Off_Stat', '0', '0', 'USLAB000080', 216),
    ('USGNC_CA_AttMnvr_In_Progress', '0', '0', 'USLAB000081', 217),
    ('Prim_CCS_MDM_Std_Cmd_Accept_Cnt', '0', '0', 'USLAB000082', 218),
    ('Prim_CCS_MDM_Data_Load_Cmd_Accept_Cnt', '0', '0', 'USLAB000083', 219),
    ('Coarse_Time', '0', '0', 'USLAB000084', 220),
    ('Fine_Time', '0', '0', 'USLAB000085', 221),
    ('Prim_CCS_MDM_PCS_Cnct_Cnt', '0', '0', 'USLAB000087', 222),
    ('Ku_HRFM_VBSP_1_Activity_Indicator', '0', '0', 'USLAB000088', 223),
    ('Ku_HRFM_VBSP_2_Activity_Indicator', '0', '0', 'USLAB000089', 224),
    ('Ku_HRFM_VBSP_3_Activity_Indicator', '0', '0', 'USLAB000090', 225),
    ('Ku_HRFM_VBSP_4_Activity_Indicator', '0', '0', 'USLAB000091', 226),
    ('Audio_IAC1_Mode_Indication', '0', '0', 'USLAB000093', 227),
    ('Audio_IAC2_Mode_Indication', '0', '0', 'USLAB000094', 228),
    ('VDS_Destination_9_Source_ID', '0', '0', 'USLAB000095', 229),
    ('VDS_Destination_13_Source_ID', '0', '0', 'USLAB000096', 230),
    ('VDS_Destination_14_Source_ID', '0', '0', 'USLAB000097', 231),
    ('VDS_Destination_29_Source_ID', '0', '0', 'USLAB000098', 232),
    ('RPCM_LAD52B_A_RPC_08_UHF_SSSR_1_On_Off_Stat', '0', '0', 'USLAB000099', 233),
    ('RPCM_LA1B_H_RPC_04_UHF_SSSR_2_On_Off_Stat', '0', '0', 'USLAB000100', 234),
    ('UHF_Frame_Sync', '0', '0', 'USLAB000101', 235),
    ('USGNC_SD_Selected_State_Time_Tag', '0', '0', 'USLAB000102', 236),
    ('USGNC_CMG1_IG_Vibration', '0', '0', 'Z1000001', 237),
    ('USGNC_CMG2_IG_Vibration', '0', '0', 'Z1000002', 238),
    ('USGNC_CMG3_IG_Vibration', '0', '0', 'Z1000003', 239),
    ('USGNC_CMG4_IG_Vibration', '0', '0', 'Z1000004', 240),
    ('USGNC_CMG1_SpinMtr_Current', '0', '0', 'Z1000005', 241),
    ('USGNC_CMG2_SpinMtr_Current', '0', '0', 'Z1000006', 242),
    ('USGNC_CMG3_SpinMtr_Current', '0', '0', 'Z1000007', 243),
    ('USGNC_CMG4_SpinMtr_Current', '0', '0', 'Z1000008', 244),
    ('USGNC_CMG1_Current_Wheel_Speed', '0', '0', 'Z1000009', 245),
    ('USGNC_CMG2_Current_Wheel_Speed', '0', '0', 'Z1000010', 246),
    ('USGNC_CMG3_Current_Wheel_Speed', '0', '0', 'Z1000011', 247),
    ('USGNC_CMG4_Current_Wheel_Speed', '0', '0', 'Z1000012', 248),
    ('eva_crew_1', '0', 'crew1', '0', 249),
    ('eva_crew_2', '0', 'crew2', '0', 250),
    ('us_eva_#', '0', '0', '0', 251),
    ('rs_eva_#', '0', '0', '0', 252),
    ('last_us_eva_duration', '0', '0', '0', 253),
    ('last_rs_eva_duration', '0', '0', '0', 254),
    ('Lightstreamer', '0', 'Unsubscribed', '0', 255),
    ('ClientStatus', '0', '0', '0', 256),
    ('MSS MT Position Float', '0', '0', 'CSAMT000001', 257),
    ('MSS MT Utility Port ID', '0', '0', 'CSAMT000002', 258),
    ('MSS EDCD SSRMS Base Location', '0', '0', 'CSASSRMS001', 259),
    ('MSS EDCD SSRMS Base Location2', '0', '0', 'CSASSRMS002', 260),
    ('MSS EDCD SSRMS Operating Base', '0', '0', 'CSASSRMS003', 261),
    ('SSRMS SR Measured Joint Position', '0', '0', 'CSASSRMS004', 262),
    ('SSRMS SY Measured Joint Position', '0', '0', 'CSASSRMS005', 263),
    ('SSRMS SP Measured Joint Position', '0', '0', 'CSASSRMS006', 264),
    ('SSRMS EP Measured Joint Position', '0', '0', 'CSASSRMS007', 265),
    ('SSRMS WP Measured Joint Position', '0', '0', 'CSASSRMS008', 266),
    ('SSRMS WY Measured Joint Position', '0', '0', 'CSASSRMS009', 267),
    ('SSRMS WR Measured Joint Position', '0', '0', 'CSASSRMS010', 268),
    ('MSS OCS Payload Status SSRMS Tip LEE', '0', '0', 'CSASSRMS011', 269),
    ('MSS OCS Base Location SPDM', '0', '0', 'CSASPDM0001', 270),
    ('MSS OCS Base Location SPDM2', '0', '0', 'CSASPDM0002', 271),
    ('MSS OCS SPDM 1 SR Measured Joint Position', '0', '0', 'CSASPDM0003', 272),
    ('MSS OCS SPDM 1 SY Measured Joint Position', '0', '0', 'CSASPDM0004', 273),
    ('MSS OCS SPDM 1 SP Measured Joint Position', '0', '0', 'CSASPDM0005', 274),
    ('MSS OCS SPDM 1 EP Measured Joint Position', '0', '0', 'CSASPDM0006', 275),
    ('MSS OCS SPDM 1 WP Measured Joint Position', '0', '0', 'CSASPDM0007', 276),
    ('MSS OCS SPDM 1 WY Measured Joint Position', '0', '0', 'CSASPDM0008', 277),
    ('MSS OCS SPDM 1 WR Measured Joint Position', '0', '0', 'CSASPDM0009', 278),
    ('MSS Payload Status OCS SPDM Arm 1 OTCM', '0', '0', 'CSASPDM0010', 279),
    ('MSS OCS SPDM 2 SR Measured Joint Position', '0', '0', 'CSASPDM0011', 280),
    ('MSS OCS SPDM 2 SY Measured Joint Position', '0', '0', 'CSASPDM0012', 281),
    ('MSS OCS SPDM 2 SP Measured Joint Position', '0', '0', 'CSASPDM0013', 282),
    ('MSS OCS SPDM 2 EP Measured Joint Position', '0', '0', 'CSASPDM0014', 283),
    ('MSS OCS SPDM 2 WP Measured Joint Position', '0', '0', 'CSASPDM0015', 284),
    ('MSS OCS SPDM 2 WY Measured Joint Position', '0', '0', 'CSASPDM0016', 285),
    ('MSS OCS SPDM 2 WR Measured Joint Position', '0', '0', 'CSASPDM0017', 286),
    ('MSS Payload Status OCS SPDM Arm 2 OTCM', '0', '0', 'CSASPDM0018', 287),
    ('MSS Payload Status OCS SPDM Arm 2 OTCM2', '0', '0', 'CSASPDM0019', 288),
    ('MSS OCS SPDM Body Roll Joint Position', '0', '0', 'CSASPDM0020', 289),
    ('MSS Payload Status OCS SPDM Body', '0', '0', 'CSASPDM0021', 290),
    ('MSS Payload Status OCS SPDM Body2', '0', '0', 'CSASPDM0022', 291),
    ('MSS OCS Payload Status MBS MCAS', '0', '0', 'CSAMBS00001', 292),
    ('MSS OCS Payload Status MBS MCAS2', '0', '0', 'CSAMBS00002', 293),
    ('MSS OCS Payload Status MBS POA', '0', '0', 'CSAMBA00003', 294),
    ('MSS OCS Payload Status MBS POA2', '0', '0', 'CSAMBA00004', 295),
]

def create_vv_database(database_path, table_name):
    # Open a connection to the database
    with sqlite3.connect(database_path) as conn:
        conn.isolation_level = None
        c = conn.cursor()

        # Set the journal mode to WAL
        c.execute("PRAGMA journal_mode=WAL")

        # Drop the table if it exists
        c.execute(f"DROP TABLE IF EXISTS {table_name}")

        # Create the table with the correct structure
        c.execute(f'''
            CREATE TABLE IF NOT EXISTS {table_name} (
                Spacecraft TEXT,
                Type TEXT,
                Mission TEXT,
                Event TEXT,
                Date DATE,
                Location TEXT,
                Arrival TEXT,
                Departure TEXT
            )
        ''')

        # Insert initial data if the table is empty
        c.execute(f"INSERT OR IGNORE INTO {table_name} (Spacecraft, Type, Mission, Event, Date, Location, Arrival, Departure) VALUES(?, ?, ?, ?, ?, ?, ?, ?)",
                  ('0', '0', '0', '0', '0', '0', '0', '0'))
    
        # Close the connection to the database
        conn.close()

def create_vv_database(database_path, table_name):
    # Open a connection to the database
    conn = sqlite3.connect(database_path)
    conn.isolation_level = None
    c = conn.cursor()

    # Set the journal mode to WAL
    c.execute("PRAGMA journal_mode=WAL")

    # Drop the table if it exists
    c.execute(f"DROP TABLE IF EXISTS {table_name}")

    # Create the table with the correct structure
    c.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            Spacecraft TEXT,
            Type TEXT,
            Mission TEXT,
            Event TEXT,
            Date DATE,
            Location TEXT,
            Arrival TEXT,
            Departure TEXT
        )
    ''')

    c.execute(f"INSERT OR IGNORE INTO {table_name} (Spacecraft, Type, Mission, Event, Date, Location, Arrival, Departure) VALUES(?, ?, ?, ?, ?, ?, ?, ?)",
                      ('0', '0', '0', '0', '0', '0', '0', '0'))

    # Close the connection to the database
    conn.close()

def create_tdrs_database(database_path, table_name):
    # Open a connection to the database
    conn = sqlite3.connect(database_path)
    conn.isolation_level = None
    c = conn.cursor()

    # Create the table and populate it with data if it doesn't already exist
    c.execute("pragma journal_mode=wal")
    c.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (`TDRS1` TEXT, `TDRS2` TEXT, `Timestamp` TEXT)")
    c.execute(f"INSERT OR IGNORE INTO {table_name} VALUES(?, ?, ?)", ('0', '0', '0'))

    # Close the connection to the database
    conn.close()

def create_iss_telemetry_database(database_path, table_name, data):
    # Open a connection to the database
    conn = sqlite3.connect(database_path)
    conn.isolation_level = None
    c = conn.cursor()

    # Create the table and populate it with data if it doesn't already exist
    c.execute("pragma journal_mode=wal")
    c.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (`Label` TEXT PRIMARY KEY, `Timestamp` TEXT, `Value` TEXT, `ID` TEXT, `dbID` NUMERIC)")
    c.executemany(f"INSERT OR IGNORE INTO {table_name} VALUES(?, ?, ?, ?, ?)", data)

    # Close the connection to the database
    conn.close()

# Define the paths to the databases
iss_telemetry_db_path = '/dev/shm/iss_telemetry.db'
tdrs_db_path = '/dev/shm/tdrs.db'
vv_db_path = '/dev/shm/vv.db'

# Remove any existing databases at startup
if os.path.exists(iss_telemetry_db_path):
    os.remove(iss_telemetry_db_path)

if os.path.exists(tdrs_db_path):
    os.remove(tdrs_db_path)

# Create the VV database and table
create_vv_database(vv_db_path, 'vv')

# Create the TDRS database and table
create_tdrs_database(tdrs_db_path, 'tdrs')

# Create the ISS telemetry database and table
create_iss_telemetry_database(iss_telemetry_db_path, 'telemetry', telemetry_data)
