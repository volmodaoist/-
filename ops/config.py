import argparse
import os, sys, time, random, warnings


warnings.filterwarnings("ignore", category=UserWarning)



# ����һ�����ڽ��������в�������
parser = argparse.ArgumentParser()

# ����ͼ���·��
parser.add_argument('--input-image', type = str, 
            help = 'Accept the path of the input image')

# ֱ������ͨ��������Ĭ��ͨ������ 3���������ͼ��
parser.add_argument('-c', '--channels',  type = int, default = 3, 
            help = 'Convert an image to grayscale or RGB')

# ������������ӣ�ʹ�� 0000-1111 ������ƣ��ĸ�λ�÷ֱ��Ӧ�������� [��˹����, ��������, ��������, ָ������]
parser.add_argument('-ns', '--noise',  type = str, default = '0000',
            help = 'Accept a mask represent four type of noise (gaussian, salt-and-pepper, Poisson or exponential noise). ')

# ��������ͼ��ĳߴ��С
parser.add_argument('-s', "--size", type = int, default = 224,
            help = 'Resize the input size of input image.')

# ������˫���˲����Ĳ��������²�����ʵҲ��һ�����ܹ���������һ���˲����� i.e.��Ϊͨ���Բ���
parser.add_argument("--radius", type = int, default = 3, 
            help = 'Specified the kernel radius of the filter') 
parser.add_argument("--sigma-color", type = int, default = 10,
            help = 'Specified the sigma-color of the bilateral kernel')
parser.add_argument("--sigma-space", type = int, default = 10,
            help = 'Specified the sigma-space of the bilateral kernel')