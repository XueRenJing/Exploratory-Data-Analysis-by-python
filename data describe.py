������numpy������һ�������,����ߴ���һ����̬�ֲ�����������ܹ�50������ʵ�顣
from numpy.random import normal, randint
datatest= normal(0, 50, size=50)
һ��������ͳ�Ƶ�ͳ�����о�ֵ����������λ���������׼�����
��������Ҫ��ͳ���������Էֱ���numpy����SciPy����pandas������

Numpy�����㷽��

from numpy import mean, median
import numpy as np
np.mean(datatest)---�����ֵ
np.median(datatest)��������λ��
np.std(datatest)�������׼��
np.var(datatest)�����㷽��

scipy�����㷽��

from scipy.stats import mode
mode(datatest)

pandas�����㷽��

��pandas����ͳ��������Ҫ�Ȱ�����ת����pandas�����ݿ��ʽ
�ȼ�������number��,תΪ�ֵ�
datatestn={'number':datatest}
��תΪdataframe��ʽ
datatestn =pd.DataFrame(datatestn)
�Ϳ���ֱ����
datatestn.mean()
datatestn.median()
datatestn.mode()
����һ����λ
datatestn.describe()



���ϣ�������������ֵ����׼������Сֵ���Լ�����λ�㡣
datatestn.skew()
datatestn.kurt()
��������Լ�Ҫ���������ݣ�������sas���洦���꣬��python��ȡ�����磺
datatestnnn=pd.read_sas(��D:\\dataplay.sas7bdat��)
datatestnnn['salary'].shape��ȡ����������ٿ�����������
Ȼ���øղ��ᵽ��һϵ�з�������������datatestnnn.skew()���������ƫ��Խ����Ϊ������˵�����ݵķֲ���β���ұߣ��ұߵļ���ֵ�϶࣬�����н϶���쳣ֵ��