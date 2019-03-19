from sklearn.ensemble import RandomForestClassifier
import scipy.io
import numpy as np
import pickle
filename = 'Forest_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))
print 'Welcome to the prediction tool: pls use the point as separator for decimal number: (3.7 and not 3,7)'
print'-------------------------\n'
Steroids= ['Daytime SBP [mmHg]',
        'Daytime DBP [mmHg]',
        'Daytime MBP [mmHg]',
        'Nighttime SBP [mmHg]',
        'Nighttime DBP [mmHg]',
        'Nighttime MBP [mmHg]',
        'Weighted BPV [mmHg]',
        'Daytime SBP Load [%]',
        'Daytime DBP Load [%]',
        'Nighttime SBP Load [%]',
        'Nighttime DBP Load [%]',
        'Reverse Dipping pattern [0=No, 1=Yes]',
        'Post-Prandial Hypotension [0=No, 1=Yes]',
        'Hypo-ep (Delta 15 / 24h) [number of episodes]',
        'Hypo-aw (Delta 15 / 24h) [0=No, 1=Yes]']
Query = np.zeros((1,15))
Prediction_type = ['OH (-)',
'OH (+)']
for i in range(len(Steroids)):
    String_to_print = 'Insert value of ' +Steroids[i]+' and press enter:\n'
    Query[0,i] = input(String_to_print)
Prediction = loaded_model.predict(Query)
print '------------'
print 'The patient is predicted as ' + Prediction_type[Prediction[0]]
