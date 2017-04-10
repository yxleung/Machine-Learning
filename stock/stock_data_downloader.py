import urllib.request as req

req_url = 'http://table.finance.yahoo.com/table.csv?s=%s.sz'
stock_code = ['000001', '000002', '000004', '000005', '000006', '000007', '000008', '000009', '000010', '000011',
              '000012', '000014', '000016', '000017', '000018   ', '000019', '000020', '000021', '000022', '000023',
              '000025', '000026', '000027', '000028', '000029', '000030', '000031', '000032', '000033', '000034',
              '000035', '000036', '000037', '000038', '000039', '000040', '000042', '000043', '000045', '000046',
              '000048', '000049', '000050', '000055', '000056', '000058', '000059', '000060', '000061',
              '000062', '000063', '000065', '000066', '000068', '000069', '000070', '000078', '000088', '000089',
              '000090', '000096', '000099', '000100', '000150', '000151', '000153', '000155', '000156', '000157',
              '000158', '000159', '000166', '000301', '000333', '000338', '000400', '000401', '000402',
              '000403', '000404', '000407', '000408', '000409', '000410', '000411', '000413', '000415', '000416',
              '000417', '000418', '000419', '000420', '000421', '000422', '000423', '000425', '000426', '000428',
              '000429', '000430', '000488', '000498', '000501', '000502', '000503', '000504', '000505', '000506',
              '000507', '000509', '000510', '000511', '000513', '000514', '000516', '000517', '000518', '000519',
              '000520', '000521', '000523', '000524', '000525', '000526', '000528', '000529', '000530', '000531',
              '000532', '000533', '000534', '000536', '000537', '000538', '000539', '000540', '000541', '000543',
              '000544', '000545', '000546', '000547', '000548', '000550', '000551', '000552', '000553', '000554',
              '000555', '000557', '000558', '000559', '000560', '000561', '000563', '000564', '000565', '000566',
              '000567', '000568', '000570', '000571', '000572', '000573', '000576', '000581', '000582', '000584',
              '000585', '000586', '000587', '000589', '000590', '000591', '000592', '000593', '000595', '000596',
              '000597', '000598', '000599', '000600', '000601', '000603', '000605', '000606', '000607', '000608',
              '000609', '000610', '000611', '000612', '000613', '000615', '000616', '000617', '000619', '000620',
              '000622', '000623', '000625', '000626', '000627', '000628', '000629', '000630', '000631', '000632',
              '000633', '000635', '000636', '000637', '000638', '000639', '000650', '000651', '000652', '000655',
              '000656', '000657', '000659', '000661', '000662', '000663', '000665', '000666', '000667', '000668',
              '000669', '000670', '000671', '000672', '000673', '000676', '000677', '000678', '000679', '000680',
              '000681', '000682', '000683', '000685', '000686', '000687', '000688', '000690', '000691', '000692',
              '000693', '000695', '000697', '000698', '000700', '000701', '000702', '000703', '000705', '000707',
              '000708', '000709', '000710', '000711', '000712', '000713', '000715', '000716', '000717', '000718',
              '000719', '000720', '000721', '000722', '000723', '000725', '000726', '000727', '000728', '000729',
              '000731', '000732', '000733', '000735', '000736', '000737', '000738', '000739', '000750', '000751',
              '000752', '000753', '000755', '000756', '000757', '000758', '000759', '000760', '000761', '000762',
              '000766', '000767', '000768', '000776', '000777', '000778', '000779', '000780', '000782', '000783',
              '000785', '000786', '000788', '000789', '000790', '000791', '000792', '000793', '000795', '000796',
              '000797', '000798', '000799', '000800', '000801', '000802', '000803', '000806', '000807', '000809',
              '000810', '000811', '000812', '000813', '000815', '000816', '000818', '000819', '000820', '000821',
              '000822', '000823', '000825', '000826', '000828', '000829', '000830', '000831', '000833', '000835',
              '000836', '000837', '000838', '000839', '000848', '000850', '000851', '000852', '000856', '000858',
              '000859', '000860', '000861', '000862', '000863', '000868', '000869', '000875', '000876', '000877',
              '000878', '000880', '000881', '000882', '000883', '000885', '000886', '000887', '000888', '000889',
              '000890', '000892', '000893', '000895', '000897', '000898', '000899', '000900', '000901', '000902',
              '000903', '000905', '000906', '000908', '000909', '000910', '000911', '000912', '000913', '000915',
              '000916', '000917', '000918', '000919', '000920', '000921', '000922', '000923', '000925', '000926',
              '000927', '000928', '000929', '000930', '000931', '000932', '000933', '000935', '000936', '000937',
              '000938', '000939', '000948', '000949', '000950', '000951', '000952', '000953', '000955', '000957',
              '000958', '000959', '000960', '000961', '000962', '000963', '000965', '000966', '000967', '000968',
              '000969', '000970', '000971', '000972', '000973', '000975', '000976', '000977', '000978', '000979',
              '000980', '000981', '000982', '000983', '000985', '000987', '000988', '000989', '000990',
              '000993', '000995', '000996', '000997', '000998', '000999', '001696', '001896', '001979', '002001',
              '002002', '002003', '002004', '002005', '002006', '002007', '002008', '002009', '002010', '002011',
              '002012', '002013', '002014', '002015', '002016', '002017', '002018', '002019', '002020', '002021',
              '002022', '002023', '002024', '002025', '002026', '002027', '002028', '002029', '002030', '002031',
              '002032', '002033', '002034', '002035', '002036', '002037', '002038', '002039', '002040', '002041',
              '002042', '002043', '002044', '002045', '002046', '002047', '002048', '002049', '002050', '002051',
              '002052', '002053', '002054', '002055', '002056', '002057', '002058', '002059', '002060', '002061',
              '002062', '002063', '002064', '002065', '002066', '002067', '002068', '002069', '002070', '002071',
              '002072', '002073', '002074', '002075', '002076', '002077', '002078', '002079', '002080', '002081',
              '002082', '002083', '002084', '002085', '002086', '002087', '002088', '002089', '002090', '002091',
              '002092', '002093', '002094', '002095', '002096', '002097', '002098', '002099', '002100', '002101',
              '002102', '002103', '002104', '002105', '002106', '002107', '002108', '002109', '002110', '002111',
              '002112', '002113', '002114', '002115', '002116', '002117', '002118', '002119', '002120', '002121',
              '002122', '002123', '002124', '002125', '002126', '002127', '002128', '002129', '002130', '002131',
              '002132', '002133', '002134', '002135', '002136', '002137', '002138', '002139', '002140', '002141',
              '002142', '002143', '002144', '002145', '002146', '002147', '002148', '002149', '002150', '002151',
              '002152', '002153', '002154', '002155', '002156', '002157', '002158', '002159', '002160', '002161',
              '002162', '002163', '002164', '002165', '002166', '002167', '002168', '002169', '002170', '002171',
              '002172', '002173', '002174', '002175', '002176', '002177', '002178', '002179', '002180', '002181',
              '002182', '002183', '002184', '002185', '002186', '002187', '002188', '002189', '002190', '002191',
              '002192', '002193', '002194', '002195', '002196', '002197', '002198', '002199', '002200', '002201',
              '002202', '002203', '002204', '002205', '002206', '002207', '002208', '002209', '002210', '002211',
              '002212', '002213', '002214', '002215', '002216', '002217', '002218', '002219', '002220', '002221',
              '002222', '002223', '002224', '002225', '002226', '002227', '002228', '002229', '002230', '002231',
              '002232', '002233', '002234', '002235', '002236', '002237', '002238', '002239', '002240', '002241',
              '002242', '002243', '002244', '002245', '002246', '002247', '002248', '002249', '002250', '002251',
              '002252', '002253', '002254', '002255', '002256', '002258', '002259', '002260', '002261', '002262',
              '002263', '002264', '002265', '002266', '002267', '002268', '002269', '002270', '002271', '002272',
              '002273', '002274', '002275', '002276', '002277', '002278', '002279', '002280', '002281', '002282',
              '002283', '002284', '002285', '002286', '002287', '002288', '002289', '002290', '002291', '002292',
              '002293', '002294', '002295', '002296', '002297', '002298', '002299', '002300', '002301', '002302',
              '002303', '002304', '002305', '002306', '002307', '002308', '002309', '002310', '002311', '002312',
              '002313', '002314', '002315', '002316', '002317', '002318', '002319', '002320', '002321', '002322',
              '002323', '002324', '002325', '002326', '002327', '002328', '002329', '002330', '002331', '002332',
              '002333', '002334', '002335', '002336', '002337', '002338', '002339', '002340', '002341', '002342',
              '002343', '002344', '002345', '002346', '002347', '002348', '002349', '002350', '002351', '002352',
              '002353', '002354', '002355', '002356', '002357', '002358', '002359', '002360', '002361', '002362',
              '002363', '002364', '002365', '002366', '002367', '002368', '002369', '002370', '002371', '002372',
              '002373', '002374', '002375', '002376', '002377', '002378', '002379', '002380', '002381', '002382',
              '002383', '002384', '002385', '002386', '002387', '002388', '002389', '002390', '002391', '002392',
              '002393', '002394', '002395', '002396', '002397', '002398', '002399', '002400', '002401', '002402',
              '002403', '002404', '002405', '002406', '002407', '002408', '002409', '002410', '002411', '002412',
              '002413', '002414', '002415', '002416', '002417', '002418', '002419', '002420', '002421', '002422',
              '002423', '002424', '002425', '002426', '002427', '002428', '002429', '002430', '002431', '002432',
              '002433', '002434', '002435', '002436', '002437', '002438', '002439', '002440', '002441', '002442',
              '002443', '002444', '002445', '002446', '002447', '002448', '002449', '002450', '002451', '002452',
              '002453', '002454', '002455', '002456', '002457', '002458', '002459', '002460', '002461', '002462',
              '002463', '002464', '002465', '002466', '002467', '002468', '002469', '002470', '002471', '002472',
              '002473', '002474', '002475', '002476', '002477', '002478', '002479', '002480', '002481', '002482',
              '002483', '002484', '002485', '002486', '002487', '002488', '002489', '002490', '002491', '002492',
              '002493', '002494', '002495', '002496', '002497', '002498', '002499', '002500', '002501', '002502',
              '002503', '002504', '002505', '002506', '002507', '002508', '002509', '002510', '002511', '002512',
              '002513', '002514', '002515', '002516', '002517', '002518', '002519', '002520', '002521', '002522',
              '002523', '002524', '002526', '002527', '002528', '002529', '002530', '002531', '002532', '002533',
              '002534', '002535', '002536', '002537', '002538', '002539', '002540', '002541', '002542', '002543',
              '002544', '002545', '002546', '002547', '002548', '002549', '002550', '002551', '002552', '002553',
              '002554', '002555', '002556', '002557', '002558', '002559', '002560', '002561', '002562', '002563',
              '002564', '002565', '002566', '002567', '002568', '002569', '002570', '002571', '002572', '002573',
              '002574', '002575', '002576', '002577', '002578', '002579', '002580', '002581', '002582', '002583',
              '002584', '002585', '002586', '002587', '002588', '002589', '002590', '002591', '002592', '002593',
              '002594', '002595', '002596', '002597', '002598', '002599', '002600', '002601', '002602', '002603',
              '002604', '002605', '002606', '002607', '002608', '002609', '002610', '002611', '002612', '002613',
              '002614', '002615', '002616', '002617', '002618', '002619', '002620', '002621', '002622', '002623',
              '002624', '002625', '002626', '002627', '002628', '002629', '002630', '002631', '002632', '002633',
              '002634', '002635', '002636', '002637', '002638', '002639', '002640', '002641', '002642', '002643',
              '002644', '002645', '002646', '002647', '002648', '002649', '002650', '002651', '002652', '002653',
              '002654', '002655', '002656', '002657', '002658', '002659', '002660', '002661', '002662', '002663',
              '002664', '002665', '002666', '002667', '002668', '002669', '002670', '002671', '002672', '002673',
              '002674', '002675', '002676', '002677', '002678', '002679', '002680', '002681', '002682', '002683',
              '002684', '002685', '002686', '002687', '002688', '002689', '002690', '002691', '002692', '002693',
              '002694', '002695', '002696', '002697', '002698', '002699', '002700', '002701', '002702', '002703',
              '002705', '002706', '002707', '002708', '002709', '002711', '002712', '002713', '002714', '002715',
              '002716', '002717', '002718', '002719', '002721', '002722', '002723', '002724', '002725', '002726',
              '002727', '002728', '002729', '002730', '002731', '002732', '002733', '002734', '002735', '002736',
              '002737', '002738', '002739', '002740', '002741', '002742', '002743', '002745', '002746', '002747',
              '002748', '002749', '002750', '002751', '002752', '002753', '002755', '002756', '002757', '002758',
              '002759', '002760', '002761', '002762', '002763', '002765', '002766', '002767', '002768', '002769',
              '002770', '002771', '002772', '002773', '002774', '002775', '002776', '002777', '002778', '002779',
              '002780', '002781', '002782', '002783', '002785', '002786', '002787', '002788', '002789', '002790',
              '002791', '002792', '002793', '002795', '002796', '002797', '002798', '002799', '002800', '002801',
              '002802', '002803', '002805', '002806', '002807', '002808', '002809', '002810', '002811', '002812',
              '002813', '002815', '002816', '002817', '002818', '002819', '002820', '002821', '002822', '002823',
              '002824', '002825', '002826', '002827', '002828', '002829', '002830', '002831', '002832', '002833',
              '002835', '002836', '002837', '002838', '002839', '002840', '002841', '002842', '002843', '002845',
              '002846', '002847', '002848', '002849', '002850', '002851', '002852', '002853', '002855', '002856',
              '002857', '002858', '300001', '300002', '300003', '300004', '300005', '300006', '300007', '300008',
              '300009', '300010', '300011', '300012', '300013', '300014', '300015', '300016', '300017', '300018',
              '300019', '300020', '300021', '300022', '300023', '300024', '300025', '300026', '300027', '300028',
              '300029', '300030', '300031', '300032', '300033', '300034', '300035', '300036', '300037', '300038',
              '300039', '300040', '300041', '300042', '300043', '300044', '300045', '300046', '300047', '300048',
              '300049', '300050', '300051', '300052', '300053', '300054', '300055', '300056', '300057', '300058',
              '300059', '300061', '300062', '300063', '300064', '300065', '300066', '300067', '300068', '300069',
              '300070', '300071', '300072', '300073', '300074', '300075', '300076', '300077', '300078', '300079',
              '300080', '300081', '300082', '300083', '300084', '300085', '300086', '300087', '300088', '300089',
              '300090', '300091', '300092', '300093', '300094', '300095', '300096', '300097', '300098', '300099',
              '300100', '300101', '300102', '300103', '300104', '300105', '300106', '300107', '300108', '300109',
              '300110', '300111', '300112', '300113', '300114', '300115', '300116', '300117', '300118', '300119',
              '300120', '300121', '300122', '300123', '300124', '300125', '300126', '300127', '300128', '300129',
              '300130', '300131', '300132', '300133', '300134', '300135', '300136', '300137', '300138', '300139',
              '300140', '300141', '300142', '300143', '300144', '300145', '300146', '300147', '300148', '300149',
              '300150', '300151', '300152', '300153', '300154', '300155', '300156', '300157', '300158', '300159',
              '300160', '300161', '300162', '300163', '300164', '300165', '300166', '300167', '300168', '300169',
              '300170', '300171', '300172', '300173', '300174', '300175', '300176', '300177', '300178', '300179',
              '300180', '300181', '300182', '300183', '300184', '300185', '300187', '300188', '300189', '300190',
              '300191', '300192', '300193', '300194', '300195', '300196', '300197', '300198', '300199', '300200',
              '300201', '300202', '300203', '300204', '300205', '300206', '300207', '300208', '300209', '300210',
              '300211', '300212', '300213', '300214', '300215', '300216', '300217', '300218', '300219', '300220',
              '300221', '300222', '300223', '300224', '300225', '300226', '300227', '300228', '300229', '300230',
              '300231', '300232', '300233', '300234', '300235', '300236', '300237', '300238', '300239', '300240',
              '300241', '300242', '300243', '300244', '300245', '300246', '300247', '300248', '300249', '300250',
              '300251', '300252', '300253', '300254', '300255', '300256', '300257', '300258', '300259', '300260',
              '300261', '300262', '300263', '300264', '300265', '300266', '300267', '300268', '300269', '300270',
              '300271', '300272', '300273', '300274', '300275', '300276', '300277', '300278', '300279', '300280',
              '300281', '300282', '300283', '300284', '300285', '300286', '300287', '300288', '300289', '300290',
              '300291', '300292', '300293', '300294', '300295', '300296', '300297', '300298', '300299', '300300',
              '300301', '300302', '300303', '300304', '300305', '300306', '300307', '300308', '300309', '300310',
              '300311', '300312', '300313', '300314', '300315', '300316', '300317', '300318', '300319', '300320',
              '300321', '300322', '300323', '300324', '300325', '300326', '300327', '300328', '300329', '300330',
              '300331', '300332', '300333', '300334', '300335', '300336', '300337', '300338', '300339', '300340',
              '300341', '300342', '300343', '300344', '300345', '300346', '300347', '300348', '300349', '300350',
              '300351', '300352', '300353', '300354', '300355', '300356', '300357', '300358', '300359', '300360',
              '300362', '300363', '300364', '300365', '300366', '300367', '300368', '300369', '300370', '300371',
              '300372', '300373', '300374', '300375', '300376', '300377', '300378', '300379', '300380', '300381',
              '300382', '300383', '300384', '300385', '300386', '300387', '300388', '300389', '300390', '300391',
              '300392', '300393', '300394', '300395', '300396', '300397', '300398', '300399', '300400', '300401',
              '300402', '300403', '300404', '300405', '300406', '300407', '300408', '300409', '300410', '300411',
              '300412', '300413', '300414', '300415', '300416', '300417', '300418', '300419', '300420', '300421',
              '300422', '300423', '300424', '300425', '300426', '300427', '300428', '300429', '300430', '300431',
              '300432', '300433', '300434', '300435', '300436', '300437', '300438', '300439', '300440', '300441',
              '300442', '300443', '300444', '300445', '300446', '300447', '300448', '300449', '300450', '300451',
              '300452', '300453', '300455', '300456', '300457', '300458', '300459', '300460', '300461', '300462',
              '300463', '300464', '300465', '300466', '300467', '300468', '300469', '300470', '300471', '300472',
              '300473', '300474', '300475', '300476', '300477', '300478', '300479', '300480', '300481', '300482',
              '300483', '300484', '300485', '300486', '300487', '300488', '300489', '300490', '300491', '300492',
              '300493', '300494', '300495', '300496', '300497', '300498', '300499', '300500', '300501', '300502',
              '300503', '300505', '300506', '300507', '300508', '300509', '300510', '300511', '300512', '300513',
              '300515', '300516', '300517', '300518', '300519', '300520', '300521', '300522', '300523', '300525',
              '300526', '300527', '300528', '300529', '300530', '300531', '300532', '300533', '300534', '300535',
              '300536', '300537', '300538', '300539', '300540', '300541', '300542', '300543', '300545', '300546',
              '300547', '300548', '300549', '300550', '300551', '300552', '300553', '300555', '300556', '300557',
              '300558', '300559', '300560', '300561', '300562', '300563', '300565', '300566', '300567', '300568',
              '300569', '300570', '300571', '300572', '300573', '300575', '300576', '300577', '300578', '300579',
              '300580', '300581', '300582', '300583', '300584', '300585', '300586', '300587', '300588', '300589',
              '300590', '300591', '300592', '300593', '300595', '300596', '300597', '300598', '300599', '300600',
              '300601', '300602', '300603', '300605', '300606', '300607', '300608', '300609', '300610', '300611',
              '300612', '300613', '300615', '300616', '300617', '300618', '300619', '300620', '300621', '300622',
              '300623', '300625', '300626', '300627', '300628', '300629', '300630', '300631', '300635', '300636']

for i in stock_code:
    url = req_url % i
    print(url)
    try:
        response = req.urlopen(url)
        file = open('a_stock_sz/' + i, 'wb')
        file.write(response.read())
        print(i, ' : ', 'success')
    except Exception as e:
        print(e)
        pass