# 不同batch_size下训练时的acc和loss曲线

loss_b16_scores_val = [0.5591198786507234, 0.524670429469683, 0.48079258230866995, 0.4542310122867071, 0.431963150585501, 0.40050297176406346, 0.38605196309135087, 0.3610290193111711, 0.34362618823656893, 0.34101171513044004, 0.3086586778568226, 0.30168719543507083, 0.29752857793911724, 0.29899601344320526, 0.28553354024123057, 0.2818537816810542, 0.2706543183989569, 0.26726326523466454, 0.25601180004387986, 0.24972019341858012, 0.24620908026407812, 0.24277210472548172, 0.23524731951550348, 0.2322543906769058, 0.22732597329825932, 0.2275615953220025, 0.2297118425049196, 0.23191211222776317, 0.22153080027003894, 0.2200603575965013, 0.21079162077062902, 0.20849360933692868, 0.20812971547449893, 0.21184773463610654, 0.21015363391156464, 0.21047857495129016, 0.20335802598489378, 0.20198273759418522, 0.19355061447137195, 0.1874396135514641, 0.1934296120995152, 0.18826060083551338, 0.18637515764013024, 0.19232819690234365, 0.18614864573669912, 0.1832365098661181, 0.18390197652362567, 0.18003485861713336, 0.17371932070759746, 0.17823288602492807, 0.1719875755883907, 0.17669444837459508, 0.17260796815368593, 0.17052254276167844, 0.1679756025543829, 0.17643873844209915, 0.1725080004395882, 0.1641457124450127, 0.168310596763303, 0.16646512944968223, 0.16691438651892293, 0.1527353727397319, 0.16812540394077058, 0.15673822768919188, 0.15321937195276567, 0.15949152488111107, 0.157215013342498, 0.1566406897071245, 0.15769505688897065, 0.15359152035254364, 0.15038647403027142, 0.14854706950561852, 0.14819782509917137, 0.14800186246303138, 0.14846476637602637, 0.1484017711943901, 0.15018558636805884, 0.14674124483031376, 0.1444484890978567, 0.14367175103847124, 0.14545213019873166, 0.14354434120795476, 0.14165175553600318, 0.1423315316923937, 0.13788801133206766, 0.14201292882918817, 0.1424195905735985, 0.13947597857020705, 0.14232563167273554, 0.138842211628748, 0.13786710758603013, 0.13547170348368648, 0.13440872586472452, 0.1357673902781485, 0.13601082052455377, 0.13557712329984248, 0.13510227121061713, 0.12931286877483547, 0.13178382176701312, 0.12841855212026507]
acc_b16_scores_val = [0.708124025677883, 0.7417287372766366, 0.7682314221788357, 0.7872856400898005, 0.7978520700222447, 0.8186384895511544, 0.8253940759014055, 0.8363069461491788, 0.850337779338162, 0.846700155918796, 0.8680062359465113, 0.8758011432737242, 0.872683180342839, 0.8737225013198007, 0.8790923263674362, 0.8777065650648206, 0.8860211328701896, 0.8872336740203031, 0.8886194353229186, 0.895548241825672, 0.894335700696208, 0.8998787459066706, 0.8991858652450381, 0.9000519660591728, 0.9045556902926736, 0.9054217911068083, 0.9021306080130963, 0.8984929845937303, 0.9021306080130963, 0.9050753507914792, 0.9135631387596751, 0.9123505976198865, 0.9123505976198865, 0.9081933137120396, 0.9081933137223643, 0.9085397540376935, 0.9146024597366369, 0.9175472025046951, 0.921704486412542, 0.9258617703203889, 0.9223973670638498, 0.9237831283664654, 0.9262082106460428, 0.9236099082036384, 0.925342109831908, 0.9277671921114853, 0.9241295686921193, 0.9260349904832158, 0.9315780356936783, 0.9303654945538896, 0.9326173566706399, 0.9296726139025818, 0.9308851550423705, 0.9326173566706399, 0.9334834574847748, 0.9305387147167166, 0.9319244760193321, 0.9343495582989095, 0.9317512558565052, 0.9353888792758712, 0.9345227784617365, 0.9430105664402572, 0.9357353196015251, 0.9378139615554486, 0.9421444656261224, 0.939892603509372, 0.9404122640081776, 0.9404122639978528, 0.9402390438350259, 0.9417980253004685, 0.9424909059517763, 0.9452624285570076, 0.9435302269390627, 0.943703447091565, 0.943357006765911, 0.9443963277428727, 0.9423176857889494, 0.9442231075800458, 0.9447427680685268, 0.9450892083941806, 0.9454356487198345, 0.9468214100224501, 0.9463017495339693, 0.9450892083941806, 0.9475142906737579, 0.9445695479056998, 0.9445695479056998, 0.9456088688826615, 0.9445695479160244, 0.9468214100327749, 0.9466481898596232, 0.9497661527905084, 0.9478607310097366, 0.9492464923020275, 0.9475142906737579, 0.9480339511622388, 0.9504590334418161, 0.9501125931161623, 0.950978693930297, 0.9525376753957396]
loss_b16_val = 0.12841855212026507
acc_b16_val = 0.9525376753957396

loss_b16_scores = [0.6527933418884985, 0.5905447926984675, 0.5533604725340965, 0.5304058431629166, 0.5090933690631945, 0.488372184180024, 0.4671346412649936, 0.44907606625276114, 0.437177768700172, 0.42036994702684266, 0.41240780489935774, 0.3994822664544175, 0.39007013839492555, 0.38573977176700786, 0.3751026663007097, 0.3694537068616677, 0.35839689546599457, 0.3550204681953689, 0.348554401381805, 0.3404068961912479, 0.3341308665114508, 0.32734357582290025, 0.32631662286135305, 0.3156592422551347, 0.31290409948742, 0.3087079144308333, 0.30623697118455195, 0.2940463835582274, 0.2964527709979068, 0.291311818450075, 0.2915249297325334, 0.2832960689938215, 0.2901712777181781, 0.28167430097848645, 0.2677405967898041, 0.26538320736875365, 0.26590252874289066, 0.2671610192303308, 0.2658719290160811, 0.2537357889615269, 0.24958476105183183, 0.258738573026909, 0.2522057422872187, 0.24877993792822017, 0.23797512950242422, 0.23884458113677906, 0.2433088095250502, 0.23907177727917917, 0.239807718587504, 0.2373641392200922, 0.23381512903390755, 0.22961467592906812, 0.23698084615848516, 0.2297409285500674, 0.222673958531703, 0.21997255612427372, 0.22333130603999793, 0.22052526522009, 0.21334432958317612, 0.21734228854227494, 0.21629645257721053, 0.21334792484193602, 0.21184046309078028, 0.20833320799868482, 0.20568889379243224, 0.1974567892499334, 0.2053983696024473, 0.20966100929572432, 0.2021046467932035, 0.2005856976335071, 0.2034226187656311, 0.20117827856752854, 0.1946294091367007, 0.19228636727921786, 0.19594235414638791, 0.18865890055120496, 0.19318934606164617, 0.18848522039794663, 0.1838376575552744, 0.17616300972957127, 0.18609826258183165, 0.18182897779083265, 0.1893972431037045, 0.18170817531406538, 0.17963031259756268, 0.17746009171478838, 0.17787465290856097, 0.1840415009104326, 0.17824070672373124, 0.17855839889832764, 0.17222974338727973, 0.17574849553282343, 0.17538158682999508, 0.17328979307906622, 0.1699957053991583, 0.1672601699622607, 0.1724426478209455, 0.16975173013045722, 0.16860029162932946, 0.16827487083538792]
acc_b16_scores = [0.6347652866793695, 0.6866880304867486, 0.7154858825567296, 0.7311623072925688, 0.7477481378832496, 0.7590507535077083, 0.7730815866966915, 0.7887147063918241, 0.795816733067729, 0.8030919799064611, 0.810886887233674, 0.8158669669149489, 0.8216265373289451, 0.8232721288758011, 0.8323228823835095, 0.8334055084011779, 0.8406807552399099, 0.8399012645071886, 0.8435388879265546, 0.8484756625671228, 0.8519833708643686, 0.8568335354235233, 0.8556209942837346, 0.8632426814481206, 0.8617703100640914, 0.8669669149489001, 0.866793694786073, 0.87294301056643, 0.8707344534903863, 0.8745452970725792, 0.8763208037415555, 0.8776199549627577, 0.8752814827645938, 0.878572665858306, 0.8856746925342109, 0.8862809631041053, 0.8908712974190196, 0.8868872336739997, 0.8894855361164039, 0.8946821410012126, 0.8951584964489867, 0.8900051966048849, 0.8929932444136498, 0.8948986662047462, 0.8998787458860211, 0.8972371384029101, 0.8991858652347133, 0.90122120214793, 0.9007448467001559, 0.9000519660488481, 0.9029534037761996, 0.9017841676771177, 0.9011345920665166, 0.904858825567296, 0.9063745019920318, 0.9094491598822103, 0.9071972977654599, 0.9091893296379698, 0.9113112766326, 0.9100121254113979, 0.9113545816733067, 0.9113978867140136, 0.9115278018361337, 0.9156850857439806, 0.9160315260696346, 0.9191494890005196, 0.9158583059068075, 0.9153819504590335, 0.9161614411917547, 0.9188896587562793, 0.9165078815174086, 0.9170275420058895, 0.9220509267278711, 0.9211848259137364, 0.9191061839598129, 0.9253421098215833, 0.9220509267278711, 0.9230902477048328, 0.9257751602286506, 0.9284600727524683, 0.9257318551879439, 0.9276805820197471, 0.9227438073791789, 0.928200242508228, 0.9261649055950113, 0.9289797332409493, 0.9278104971418674, 0.9279837173046943, 0.9288065130781223, 0.9278538021825741, 0.9304954096656851, 0.9293694786073099, 0.9309284600727524, 0.9311449852762862, 0.9312315953576996, 0.9335267625151568, 0.9304521046249783, 0.9335267625151568, 0.9330937121080893, 0.9311882903169929]
loss_b16 = 0.1672601699622607
acc_b16 = 0.9335267625151568
train_time_b16 = 4559.486124515533

loss_b16_nodrop = 0.069
acc_b16_nodrop = 0.974

loss_b16_val_nodrop = 0.130
acc_b16_val_nodrop = 0.9586



loss_b32_scores_val = [0.5704166854396346, 0.5406137149327346, 0.5100638848511161, 0.4852831388973558, 0.4599295959519324, 0.43951907456076045, 0.4202857930274516, 0.4020414055735983, 0.39877273959798004, 0.3791957865311867, 0.3630077971415567, 0.35481516830784476, 0.348197827182443, 0.3284932824854171, 0.3276647115350492, 0.3159493550815678, 0.30287366446250236, 0.29551836777534596, 0.299234935001672, 0.28425128019993834, 0.27710427608416477, 0.2692666196149948, 0.2757324263435415, 0.2627402701525306, 0.2585383298625034, 0.2574642646380857, 0.24774173648068712, 0.24009233368304167, 0.23648708246721875, 0.24315306401306436, 0.23713390486049998, 0.22997236506851793, 0.22720524718768464, 0.21896325338553788, 0.22509643644553917, 0.2151432369912949, 0.2130884818336527, 0.21144535347739313, 0.2154032740346402, 0.20368883036439678, 0.20250536005046407, 0.20309259389005582, 0.2001835879834752, 0.1972374809112496, 0.20354127862229207, 0.19765082001686096, 0.19489309608306501, 0.1908739905577897, 0.18984343991439842, 0.18854734879235513, 0.1855105663603438, 0.18900101589677487, 0.18038800510545755, 0.173101761075543, 0.1799386519865789, 0.1776906928848027, 0.17322739858097042, 0.17112202566293214, 0.17290807398068064, 0.1685441447031182, 0.17152708586613186, 0.1679904019421687, 0.16546643242335457, 0.16857547291163946, 0.16365543261322676, 0.1613087629540921, 0.15890123948736207, 0.164279128146217, 0.16293765322372858, 0.16611547730688864, 0.15958032849837317, 0.15453731936783183, 0.15577213332720363, 0.15557498383022317, 0.15410693059259986, 0.15500620536657175, 0.1509497655897935, 0.15033673234483966, 0.1477544575790258, 0.15228043534035868, 0.14996340355653398, 0.14831108541437438, 0.14637548367918912, 0.13811893345845874, 0.14679790274142476, 0.14231407066761012, 0.146346855851201, 0.14874017658833302, 0.14635770925508304, 0.1420855115155052, 0.1442581974002201, 0.14172618598308592, 0.13955674436741594, 0.13810031159114491, 0.14018775276206052, 0.13971632966833347, 0.13832092589219439, 0.1372448006938777, 0.13588358436561263, 0.13615820243136423]
acc_b32_scores_val = [0.7115884289344221, 0.7297765460415768, 0.7481378832909091, 0.7684046423416626, 0.7827819158562997, 0.7956002079054943, 0.8065130781635923, 0.818465269398652, 0.8201974710269216, 0.8324961025773105, 0.8423696518584469, 0.84306253249943, 0.8482591373842385, 0.8586523471538557, 0.8558808245486245, 0.8655811536669339, 0.8735492811569737, 0.8754547029480702, 0.8747618222967624, 0.8815174086366888, 0.8874068941728053, 0.8880997748344378, 0.8877533344984592, 0.892083838569133, 0.891910618406306, 0.8912177377549982, 0.8960679023141529, 0.9010912870361345, 0.9009180668733076, 0.8990126450822111, 0.9035163693157119, 0.9061146717581162, 0.9036895894785388, 0.9107916161544439, 0.9076736532235588, 0.914082799248156, 0.9146024597366369, 0.9126970379455404, 0.9125238177827134, 0.9172007621790411, 0.9177204226675221, 0.9158150008764255, 0.9170275420162142, 0.9191061839701377, 0.9166811016905603, 0.9192794041329646, 0.921184825924061, 0.9192794041329646, 0.9237831283664654, 0.9263814308088697, 0.9230902477151576, 0.9222241469010228, 0.925342109831908, 0.9312315953680244, 0.9282868525999661, 0.9258617703203889, 0.9300190542282357, 0.9300190542282357, 0.9314048155308513, 0.9320976961821591, 0.9340031179732556, 0.9314048155308513, 0.9345227784617365, 0.9327905768334669, 0.9350424389502173, 0.9364282002528329, 0.9352156591130443, 0.9355620994386982, 0.9364282002528329, 0.9357353196015251, 0.9390265026952372, 0.9385068422067564, 0.9383336220439294, 0.9390265026952372, 0.9378139615554486, 0.939892603509372, 0.9419712454632955, 0.9395461631837181, 0.9426641261146033, 0.9393729430208911, 0.9423176857889494, 0.9417980253004685, 0.9421444656261224, 0.9464749696967962, 0.9419712454632955, 0.9449159882313537, 0.9430105664402572, 0.9416248051376416, 0.9445695479056998, 0.9452624285570076, 0.9440498874172188, 0.9450892083941806, 0.9459553092083154, 0.9468214100224501, 0.9466481898596232, 0.9456088688826615, 0.9480339511622388, 0.9478607309994118, 0.9478607309994118, 0.9463017495339693]
loss_b32_val = 0.13588358436561263
acc_b32_val = 0.9480339511622388

loss_b32_scores = [0.6766838007734819, 0.6027219656454139, 0.573415045182337, 0.5548398240422451, 0.5326082236005263, 0.5104185437156694, 0.4932038213379478, 0.47592822346554337, 0.46575693379091926, 0.45173530922529914, 0.4407452734239837, 0.4280608672988739, 0.4204143134907092, 0.4074873431611057, 0.3999239732100772, 0.39002508033443195, 0.3795966083413287, 0.3729466335851523, 0.3643782261585458, 0.3543005572093456, 0.3524901535540752, 0.3416271704993916, 0.3406082783355759, 0.3279770563157989, 0.32674925868936167, 0.3200986295571964, 0.3156265030075726, 0.3101256244696345, 0.3024693104086314, 0.2986962452321785, 0.2927513224257148, 0.29065381260238693, 0.28502775619518567, 0.2788577719699484, 0.27674882402251544, 0.26986579887379236, 0.2689623490128219, 0.2642207460801564, 0.26326553025114335, 0.2590918761490743, 0.25749719967859447, 0.25530492585741543, 0.24603294511870125, 0.24651166813203826, 0.24896324903454337, 0.23945384789190485, 0.23894207816323848, 0.23832919843922076, 0.22932442529722286, 0.2268296233263004, 0.2283292030252577, 0.22272242794628677, 0.22041428579824462, 0.21440078444338828, 0.2159325804038042, 0.21743244175613186, 0.21429741031558183, 0.21134850747783945, 0.20916767008234802, 0.20869406512874716, 0.20774117896838926, 0.20497772276721588, 0.1991309362465105, 0.19884190551850156, 0.1983740951342577, 0.19494081820428588, 0.1919967480740761, 0.18974566159206227, 0.19514991908816393, 0.1918827703646269, 0.18954637529360407, 0.1834266721859004, 0.1875314178426324, 0.18138632314722025, 0.18028662713441695, 0.18432675725342434, 0.17678159730863513, 0.1751301231250882, 0.17226111209260392, 0.1762894656526584, 0.17448737773906828, 0.1723811924999598, 0.1715272848158636, 0.16925695429078713, 0.1696490914896892, 0.16574065731836732, 0.1673630185976364, 0.1641630406409022, 0.15807493861132926, 0.1644380196216572, 0.1577155223155319, 0.16016288201306736, 0.15208921050170504, 0.15551921368811958, 0.15306769522310604, 0.15241318789213798, 0.15330311774216346, 0.14834795160086464, 0.1471527617611217, 0.14358252842252225]
acc_b32_scores = [0.6240689416248051, 0.6736099081726642, 0.7009786939406217, 0.7132340204193297, 0.7302529014480521, 0.7492638143183101, 0.7595271089451577, 0.769530573358739, 0.774424042937951, 0.7838645418533188, 0.7901870777655284, 0.7956435129049021, 0.8039147756695644, 0.8120561233534054, 0.8132253594318378, 0.8204139961788317, 0.8254373809008133, 0.8297678849714871, 0.8355274554061328, 0.8383422830210966, 0.8415901610947514, 0.8485189675975048, 0.8490386281169598, 0.8558808245073256, 0.8529360817702416, 0.8583925168683164, 0.8595617529777231, 0.8649315780253586, 0.8679629308954797, 0.8703014031039683, 0.8722501299047974, 0.8743287718483961, 0.8758011432633994, 0.8810410531682653, 0.8797419019677125, 0.8834228304174606, 0.8836826606513764, 0.8852416421374684, 0.8855014723507346, 0.8869738437347636, 0.8893123159742264, 0.8928633293121789, 0.8942490905734957, 0.8948986661840967, 0.8936428200242508, 0.901134592087166, 0.8986228997261752, 0.8988394248987347, 0.9036895894475646, 0.9056816213613735, 0.9042092499360455, 0.9075004330504071, 0.9108782262461821, 0.9110514463677102, 0.9104018707571091, 0.9102719556349889, 0.9110081413579776, 0.9145591546752807, 0.9136930538508212, 0.9130001731995133, 0.9142127143496268, 0.9142127143393021, 0.9181534730436153, 0.9178936427993748, 0.9188463536949231, 0.9204486402217218, 0.9227005023178227, 0.9219643166671071, 0.9209249956591712, 0.9220509267485206, 0.921574571280097, 0.9258184652693574, 0.9223540620024936, 0.9268144812056124, 0.9258617703307136, 0.925472024923054, 0.928286852568992, 0.9287199030173583, 0.9291529533934515, 0.9278538021825741, 0.9298891391164402, 0.9292395634955144, 0.9303654945538896, 0.9320543911311276, 0.931707950795149, 0.9319677810393895, 0.9328338818535242, 0.9340897280236949, 0.9363848951811521, 0.9335700675558635, 0.937164385924198, 0.9377273514843598, 0.9390265026745878, 0.937164385924198, 0.9378572665755058, 0.9410618395981292, 0.9387666724303474, 0.9406720942214438, 0.940975229506391, 0.9414948899948719]
loss_b32 = 0.14358252842252225
acc_b32 = 0.9414948899948719
train_time_b32 = 3243.437413454056



loss_b64_scores_val = [0.5922897158762662, 0.5690522922214882, 0.5493116441971504, 0.5334098282707805, 0.5190588722407828, 0.5039901351951426, 0.4880602696874041, 0.4750764001475119, 0.4623850610667945, 0.4471425305624139, 0.43498832895956896, 0.4246143595548306, 0.41082453081394305, 0.3963974690583928, 0.3935888312665383, 0.37785279298600966, 0.3655864821858904, 0.35850028181311455, 0.3516350281149763, 0.3395127625734249, 0.33366902565163176, 0.32785263870259246, 0.32509123875841656, 0.31896946734475984, 0.3085239411288317, 0.30643023385572904, 0.3000441282063532, 0.29663428781393103, 0.29261636026765037, 0.28622751442559685, 0.27823610769779333, 0.2784708546287118, 0.26811560533105777, 0.26647960823226097, 0.2692577933472198, 0.26109656614632, 0.26039185968259787, 0.25546208777729984, 0.25417836404086275, 0.25248990572760555, 0.24430992243795033, 0.24784511462997444, 0.23863419085591334, 0.235876908551959, 0.2319628961543039, 0.23403619597611922, 0.2379676333523573, 0.2266427318268873, 0.22709621871320995, 0.23019164850202606, 0.22295993485980198, 0.22499495123672913, 0.2188364842230002, 0.21545681685710025, 0.2157642921200869, 0.211666727972551, 0.2136737944533419, 0.2149748266073647, 0.20703270091313372, 0.21167047849131812, 0.20756411652579043, 0.2039883506271221, 0.20523278309116533, 0.20221830029205126, 0.2006035660326264, 0.2064440832040183, 0.19744096894869664, 0.190475303730683, 0.19675733786861632, 0.19829560840809218, 0.19391216599670746, 0.19431880959476608, 0.18837933964277498, 0.1882186679044671, 0.18781709207440297, 0.19338325196714184, 0.19218601761606813, 0.18352269224477932, 0.1815705618153365, 0.18127086118480557, 0.18486484855274052, 0.17978338347694686, 0.17683331525121346, 0.1762838019266216, 0.18196452742388605, 0.17411725964121652, 0.17488931832106216, 0.1721798158612921, 0.17546806107479263, 0.17478462167325556, 0.17424826576167493, 0.16949688769824042, 0.16722394966612486, 0.16343064945098867, 0.1668822060894268, 0.16648595429222568, 0.1683309194576218, 0.16262249804732498, 0.164980911308241, 0.1634487650040508]
acc_b64_scores_val = [0.6854321843578769, 0.706911484548419, 0.7174779144808632, 0.7278711242504804, 0.736705352554655, 0.7521219470462538, 0.7604365148516228, 0.7696171834814514, 0.7808764940652033, 0.7942144466028787, 0.7973324095337638, 0.8053005370238037, 0.8106703620714392, 0.8208903516782294, 0.8240083146091146, 0.834574744531234, 0.8390784687647348, 0.840983890566156, 0.8449679542905265, 0.8546682834088358, 0.8574398060140671, 0.8598648882936444, 0.8607309891077792, 0.8622899705732218, 0.868872336760646, 0.8702580980632616, 0.8744153819711085, 0.8745886021339354, 0.8758011432633994, 0.8790923263674362, 0.8808245279957058, 0.8822102892879966, 0.8894855361267286, 0.8886194353125939, 0.8856746925445357, 0.888446215149767, 0.8913909579178252, 0.8917373982434791, 0.8913909579178252, 0.8936428200345755, 0.899359085407865, 0.8952018015000182, 0.9017841676874423, 0.9047289104555005, 0.9050753507811544, 0.902996708827231, 0.9003984063848267, 0.9078468733863857, 0.9040360298041927, 0.9049021306183275, 0.9066343322465971, 0.9085397540376935, 0.9097522951774821, 0.9095790750146552, 0.910618395991617, 0.9116577169685787, 0.9109648363172709, 0.9114844968057517, 0.9130434782711943, 0.9121773774570595, 0.9139095790853291, 0.9151221202251177, 0.9161614412020794, 0.9152953403879447, 0.918066862993176, 0.9130434782711943, 0.9196258444586185, 0.9208383855984071, 0.9201455049470993, 0.9184133033188299, 0.9234366880408115, 0.9234366880408115, 0.9263814308088697, 0.924822449343427, 0.9236099082036384, 0.9222241469010228, 0.9246492291806001, 0.925515329994735, 0.9260349904832158, 0.9274207517858314, 0.9244760090177732, 0.9296726139025818, 0.9289797332512739, 0.9305387147167166, 0.929152953414101, 0.9305387147167166, 0.932963796996294, 0.9317512558565052, 0.9319244760193321, 0.9303654945538896, 0.9315780356936783, 0.9334834574847748, 0.9333102373219478, 0.9352156591130443, 0.9345227784617365, 0.9334834574847748, 0.9350424389502173, 0.9391997228580642, 0.9364282002528329, 0.9366014204156599]
loss_b64_val = 0.16262249804732498
acc_b64_val = 0.9391997228580642

loss_b64_scores = [0.7026198661535922, 0.6264126362243889, 0.5995452667612479, 0.5859911143418389, 0.5717374199848747, 0.5581895658343374, 0.5478361223880946, 0.5338175063031645, 0.5248533980738614, 0.5077424659155775, 0.49904883424103746, 0.4874378573681811, 0.4783523733810393, 0.46776144345133347, 0.45527508605523886, 0.44545811470988383, 0.4348527001494162, 0.43424444101142984, 0.4230692976736927, 0.4113109690590043, 0.40795210942370463, 0.3955357874800588, 0.39032206411649134, 0.384389937383431, 0.3774908735158227, 0.3749727797006458, 0.3671154998760382, 0.3592931632821737, 0.3530500485458057, 0.34860817398104826, 0.3442057273725734, 0.3370091098444767, 0.3314384516904822, 0.32437097760413935, 0.3224877911538696, 0.3190099653969723, 0.3114400095766594, 0.3130491374580942, 0.30819231631560484, 0.305395060615566, 0.2966448953860805, 0.2959486713277061, 0.2953684321520297, 0.29039369058138204, 0.2877678190161652, 0.27647153689628784, 0.2847345400218965, 0.27472294085715065, 0.2758146350147942, 0.26897087669467545, 0.26635655332547054, 0.26581437082755677, 0.26331666483120014, 0.2623603163409972, 0.2568601119328305, 0.2561469746254437, 0.25206478506135666, 0.24911628729618135, 0.2510375184965737, 0.24392623853770198, 0.23978490374560335, 0.2345991581755826, 0.24197129192559616, 0.23717144259687067, 0.23156944012778194, 0.22814039903291689, 0.22790695726613372, 0.23247809793039312, 0.2226048101177873, 0.22230364856430052, 0.22216924949099529, 0.22009470171435297, 0.21626683166478053, 0.2141407259142876, 0.21361795891958446, 0.21410226588818718, 0.20937542358944738, 0.20765543247547427, 0.2082555250518144, 0.20484345408229757, 0.2034995544881852, 0.1974102302071913, 0.20052521786944985, 0.196897535029429, 0.19388282605944238, 0.19399831004836995, 0.19738339994760273, 0.19379890780194511, 0.19373315171623032, 0.1905286539479556, 0.19026558849461753, 0.18929874099159952, 0.18578540356841056, 0.19110637808742256, 0.18314028303007432, 0.177553803226821, 0.1823321115654675, 0.1802362358262422, 0.1817404092411307, 0.17957268773260138]
acc_b64_scores = [0.596959986101088, 0.6546856053425207, 0.6769877013684393, 0.6875541313421824, 0.6999826780250162, 0.7104191928250154, 0.7201195218813764, 0.7298198509687116, 0.7349298458960034, 0.7490039840947192, 0.7519054217291481, 0.7621254114185362, 0.7681015070773649, 0.7752901438037093, 0.7822189503271122, 0.7866793694476332, 0.7939979213890203, 0.7943876667244067, 0.800493677495031, 0.806946128560335, 0.8088082452384516, 0.8179889139302285, 0.8187684046010014, 0.8219296726138923, 0.8264333968267435, 0.827992378333485, 0.8340550839911295, 0.8377793174712596, 0.8416767711245413, 0.8401610947307796, 0.8447947340864006, 0.8494283734213721, 0.8490386280550115, 0.8562272648742784, 0.857916161430867, 0.8595184480092894, 0.8635458167846913, 0.8627663260519701, 0.8618136151254476, 0.8672267452550888, 0.8712541139272435, 0.869565217442928, 0.8694353023208078, 0.8748917374498568, 0.8762774987421477, 0.8813008834331552, 0.8736358912693614, 0.8818205439526102, 0.8831630001938696, 0.8819504589818079, 0.8871470638666165, 0.886627403440084, 0.8877533345294333, 0.8893556210355826, 0.8903083318382083, 0.8915208730709195, 0.8916507882033645, 0.8948120561026833, 0.8927767191997913, 0.8952884115917563, 0.8986662047978561, 0.9023471332269547, 0.8986662047978561, 0.9002251862323245, 0.9019140828508615, 0.9032998440915287, 0.9043824700575736, 0.9039494197537534, 0.9070240776439319, 0.9058981464926341, 0.9083665338335677, 0.9087562792722014, 0.9091893296173204, 0.910488480900471, 0.9110514464399833, 0.9117443270499922, 0.9139528841260358, 0.9134332236065807, 0.9139095790233807, 0.9124805127729809, 0.9155984756109435, 0.918889658766604, 0.9159016109268648, 0.9189762687860691, 0.9210982158736218, 0.9204053352016646, 0.9181967780533478, 0.9196258444586185, 0.9191927940825253, 0.9215745712904218, 0.922787112368262, 0.9217044863815678, 0.9241728737638002, 0.9216178763311285, 0.9247358392620136, 0.9269010913283248, 0.9261649056466349, 0.925645245044582, 0.9257318551672944, 0.926814481215937]
loss_b64 = 0.177553803226821
acc_b64 = 0.9269010913283248
train_time_b64 = 3638.715329885483



loss_b8_scores_val = [0.5624297915516002, 0.5223892765587833, 0.4976648448937567, 0.4769896992814411, 0.44266523467530083, 0.42422076251835955, 0.3929206734768712, 0.38064401443591467, 0.3785671710647951, 0.35543620766045503, 0.3521793076912741, 0.3438654131303312, 0.3291923990339252, 0.32071283202835826, 0.3158430954044249, 0.3057367203503243, 0.30339979522463234, 0.3122965287428143, 0.29734885818816215, 0.2913378475754343, 0.2888253840348263, 0.28978236847912525, 0.28357390880006533, 0.2766383879419714, 0.26857471447479947, 0.28087813560892055, 0.26332627308858075, 0.26164439355926455, 0.26734429233391777, 0.2672544275438705, 0.25823973326011523, 0.261958664283479, 0.25968985473125705, 0.25148265248059026, 0.2513503250778083, 0.25305879821237154, 0.2509253425396193, 0.2570289578421079, 0.2463533580187039, 0.24183434736588252, 0.24131737499990352, 0.25009870120057526, 0.24197348147222864, 0.23804316423974045, 0.23172243891928196, 0.23546054458806073, 0.24755156115691213, 0.23481541511175352, 0.23853806342504352, 0.23751123094918017, 0.23135193006022436, 0.2358222560072697, 0.2233875497837486, 0.22698652377378253, 0.21655208511620364, 0.2133990698686799, 0.22571459453873674, 0.22411329432142352, 0.21539068834689343, 0.21431147591861843, 0.22070000083204286, 0.2145503995678422, 0.21835017954376032, 0.21374469320519676, 0.21317996071655126, 0.20281855215310596, 0.2232079004332302, 0.2144326589409202, 0.2039945455790392, 0.20666314181015888, 0.20104454977351707, 0.2037966301783767, 0.21309900499471196, 0.20087685444270142, 0.20238968245872235, 0.20081950477622068, 0.20869407162816236, 0.21330012945323104, 0.2020752840860452, 0.20922171150777982, 0.20629631535377738, 0.21136506999073792, 0.21003134127286202, 0.20210980251625055, 0.20121108664681422, 0.19867831130834546, 0.20535738450256766, 0.1921263747026948, 0.20552109300228125, 0.2050042588663188, 0.19493268730811594, 0.20098344718841565, 0.198544010617421, 0.19787014159377972, 0.1991926196071442, 0.21359896113156818, 0.1981096525702199, 0.1978525913969165, 0.20081791015451256, 0.1951063756430746]
acc_b8_scores_val = [0.7088169063085413, 0.7422483977238186, 0.7580114325410713, 0.7756798891494205, 0.7992378312938861, 0.8092846007378494, 0.8290316993001221, 0.8387320284184314, 0.8321496622310072, 0.848085917211087, 0.8484323575367408, 0.8518967607932799, 0.8593452277948388, 0.8607309890974545, 0.8631560713770318, 0.8712974190298987, 0.869911657727283, 0.86610081414509, 0.8719902996812064, 0.877013684403188, 0.8783994457058036, 0.8730296206581681, 0.8783994457058036, 0.8797852070084193, 0.8834228304277854, 0.8742421617979568, 0.8889658756382478, 0.8849818118932279, 0.8835960505906123, 0.884635371567574, 0.8867140135214975, 0.8861943530330165, 0.8896587562895556, 0.8945089208487104, 0.8943357006858833, 0.8938160401974025, 0.8908712974293443, 0.8912177377549982, 0.9002251862219998, 0.8976268837795954, 0.8974536636167685, 0.8945089208487104, 0.8964143426398068, 0.9007448467104806, 0.9042092499670197, 0.9023038281759233, 0.8943357006858833, 0.9019573878502692, 0.8986662047565572, 0.9009180668733076, 0.9019573878502692, 0.8983197644309033, 0.9081933137120396, 0.9057682314324622, 0.9097522951774821, 0.9146024597366369, 0.906807552409424, 0.9066343322465971, 0.9123505976198865, 0.9120041572942326, 0.9036895894785388, 0.9125238177827134, 0.9076736532235588, 0.9107916161544439, 0.9118309371314056, 0.9163346613649064, 0.9052485709439814, 0.91044517582879, 0.9163346613649064, 0.917893642830349, 0.9170275420162142, 0.9159882210392525, 0.9095790750146552, 0.9182400831560029, 0.9158150008764255, 0.9192794041329646, 0.9113112766429248, 0.9094058548518282, 0.9170275420162142, 0.9126970379455404, 0.9175472025046951, 0.9111380564904226, 0.9133899185968481, 0.9151221202251177, 0.9147756798994638, 0.9184133033188299, 0.9146024597366369, 0.9229170275523306, 0.9135631387699998, 0.9147756799097886, 0.9237831283664654, 0.9175472025046951, 0.917893642830349, 0.9184133033188299, 0.917893642830349, 0.9113112766429248, 0.9187597436444838, 0.9185865234816568, 0.9189329638073107, 0.9196258444586185]
loss_b8_val = 0.1921263747026948
acc_b8_val = 0.9237831283664654

loss_b8_scores = [0.6531710465332674, 0.5965804403872665, 0.5721013961869964, 0.5534419680093947, 0.5353389886776868, 0.5237306288080366, 0.5066529333503701, 0.4971219925843883, 0.483741767486377, 0.4753567080873149, 0.4678105148077837, 0.4546243499583106, 0.44700797606842285, 0.44316543704010103, 0.4352018154025718, 0.4321686796742049, 0.42519963385946064, 0.41907359247973325, 0.41090063960981105, 0.410746704955438, 0.4051544635341916, 0.39771374862040326, 0.39710912759395317, 0.3866273044504802, 0.3884796827177169, 0.38253911608491636, 0.3796173509035473, 0.37965432115811604, 0.3775860653658137, 0.3770892001183859, 0.36819186867852777, 0.3741150306827808, 0.3577060500273109, 0.3603187988422038, 0.3659016580169089, 0.3594127759549082, 0.35689705204448996, 0.3572928428394365, 0.3544927949475267, 0.35173486490638256, 0.3460082554924835, 0.34641919352298756, 0.34135802718298536, 0.3432101624952163, 0.33692294146130614, 0.3435021743917876, 0.3370495116224885, 0.33654184240661333, 0.336301006546456, 0.33534541017578023, 0.3315204777573354, 0.32963576354247726, 0.3295225919657154, 0.334295478662182, 0.3231698391785164, 0.3264899510511457, 0.32817742670148164, 0.3201681083642887, 0.31428393183920383, 0.31864884448370484, 0.318083420880468, 0.3229190561628086, 0.3252314344131098, 0.3202119546603794, 0.3184103746778286, 0.31360203617847854, 0.30941580278805714, 0.3130632678978306, 0.30670324725510445, 0.30589313614353986, 0.30526692717338216, 0.3044945059956235, 0.3107320748188251, 0.2983639018041292, 0.30186977667810494, 0.3019614159511091, 0.3036655576436003, 0.30018968776929283, 0.3018801220028524, 0.3003950853419561, 0.2998781248384423, 0.3049860834493322, 0.309018676407492, 0.2975331938438532, 0.3005245672040386, 0.3012251467049566, 0.30157954858578245, 0.29871603148824344, 0.30129263957321295, 0.2961379425203637, 0.3026608945238834, 0.28259710039121994, 0.2949544202872543, 0.2915668451228377, 0.2988198676782022, 0.29113512643219774, 0.2949791765777775, 0.2987799295171819, 0.29200924136275, 0.2901502239319278]
acc_b8_scores = [0.628875801143253, 0.6802355794214446, 0.7021479300190542, 0.7157890178416768, 0.729473410705006, 0.7377013684392864, 0.7519487268318032, 0.7556729603325827, 0.7675818465269357, 0.7679715918932963, 0.7749437034470812, 0.7830417460592413, 0.791702754200589, 0.7956002078641954, 0.7954269877013684, 0.7970292742075178, 0.8045210462497835, 0.8063398579594665, 0.8140914602459727, 0.808894855361164, 0.8142213753680928, 0.8216698423696518, 0.8187684046423004, 0.8241382296899359, 0.8234453490386281, 0.8305473757145332, 0.8308072059587736, 0.830417460592413, 0.8308938160401871, 0.828425428719903, 0.8353975402736878, 0.8351377100294475, 0.8415468560540447, 0.8397280443443617, 0.8375627923090248, 0.8432357526416074, 0.8430192274380738, 0.8427593971938334, 0.8424562619088862, 0.8455309197990646, 0.8473064264680409, 0.8472631214273342, 0.8527628615970899, 0.8511172700502339, 0.8574831110341243, 0.8500346440325653, 0.854235232981119, 0.8549281136324268, 0.8509007448467002, 0.8551013337952538, 0.8545383682660662, 0.8561839598129223, 0.8544950632253594, 0.8557942144465616, 0.8602113285986489, 0.8577862463190715, 0.8551013337952538, 0.8607742941278365, 0.8651914082799238, 0.861856920145505, 0.8625498007968128, 0.8597349731508748, 0.8593885328252209, 0.8620301403083319, 0.8647150528321497, 0.8635458167330677, 0.8667070847046596, 0.863675731855188, 0.8703447081240256, 0.8696951325134246, 0.8718603845487615, 0.8703014030833189, 0.8650181881170969, 0.8734626710549108, 0.8702580980426121, 0.8731162307292569, 0.8693486921877707, 0.8722934349558289, 0.8713407240602806, 0.8687424216178763, 0.8726831803221895, 0.868309371210809, 0.8679196258444483, 0.8738091113805647, 0.8722068248744154, 0.8726831803221895, 0.8719036895894682, 0.8747185172354062, 0.8698683526762515, 0.8740256365840984, 0.8680928460072752, 0.8821669842369652, 0.8748051273168197, 0.8740689416248051, 0.8708210635717998, 0.8757145331716611, 0.8759743634159016, 0.8715572492638143, 0.8756712281309544, 0.8771002944742768]
loss_b8 = 0.28259710039121994
acc_b8 = 0.8821669842369652
train_time_b8 = 7069.002284288406


import matplotlib.pyplot as plt

plt.plot(loss_b8_scores_val, 'r-', label='batch_size=8')
plt.plot(loss_b16_scores_val, 'g-.', label='batch_size=16')
plt.plot(loss_b32_scores_val, 'b--', label='batch_size=32')
plt.plot(loss_b64_scores_val, 'k:', label='batch_size=64')

plt.xlabel('训练轮数 Epochs')
plt.ylabel('损失值 Loss')
plt.legend(loc=0)
plt.savefig('val.png')
plt.show()

plt.plot(acc_b8_scores_val, 'r-', label='batch_size=8')
plt.plot(acc_b16_scores_val, 'g-.', label='batch_size=16')
plt.plot(acc_b32_scores_val, 'b--', label='batch_size=32')
plt.plot(acc_b64_scores_val, 'k:', label='batch_size=64')
plt.xlabel('训练轮数 Epochs')
plt.ylabel('准确率 Accuracy')
plt.legend(loc=0)
plt.savefig('train.png')
plt.show()
