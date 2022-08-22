import requests
import json
import re
import  sys

def getApiInfo_post(host, port, api, post_headers, requestBody):
    # 测试一下header是否正确
    # print(post_headers)
    response = requests.post(host + ':' + str(port) + '/' + api, data=json.dumps(requestBody), headers=post_headers)
    # 将返回的内容转换成对象
    return json.loads(response.text)


def getApiInfo_get(url, post_header):
    # 测试一下header是否正确
    # print(post_headers)
    response = requests.get(url, headers=post_headers)
    # 将返回的内容转换成对象
    return json.loads(response.text)

def qcToJson(qc_file,qc_json_file):
    # 文件路径
    path=qc_file
    qc_json_file=qc_json_file
    # 读取文件
    with open(path, 'r', encoding="utf-8") as file:
        # 定义一个用于切割字符串的正则
        seq = re.compile("\t")
        result = []
        # 逐行读取
        next(file)
        for line in file:
            lst = seq.split(line.strip())
            item = {
                "experimentId": lst[0],
                "sampleName": lst[1],
                "panelInformation": lst[2],
                "averageDepth": lst[3],
                "ontargetReadsRatio": lst[4],
                "mappedRatio": lst[5],
                "uniformity": lst[6],
                "ontargetCoverage": lst[7],
                "rawR1Bases": lst[8],
                "rawR1Q30Bases": lst[9],
                "rawR1Q30Percent": lst[10],
                "rawR1Q20Bases": lst[11],
                "rawR1Q20Percent": lst[12],
                "rawR2Bases": lst[13],
                "rawR2Q30Bases": lst[14],
                "rawR2Q30Percent": lst[15],
                "rawR2Q20Bases": lst[16],
                "rawR2Q20Percent": lst[17],
                "cleanR1Bases": lst[18],
                "cleanR1Q30Bases": lst[19],
                "cleanR1Q30Percent": lst[20],
                "cleanR1Q20Bases": lst[21],
                "cleanR1Q20Percent": lst[22],
                "cleanR2Bases": lst[23],
                "cleanR2Q30Bases": lst[24],
                "cleanR2Q30Percent": lst[25],
                "cleanR2Q20Bases": lst[26],
                "cleanR2Q20Percent": lst[27],
                "averageReadLength": lst[28],
                "averageBaseQuality": lst[29],
                "averageInsertSize": lst[30],
                "duplicationRate": lst[31],
                "rawReads": lst[32],
                "rawBases": lst[33],
                "cleanReads": lst[34],
                "cleanBases": lst[35],
                "mappedReads": lst[36],
                "mappedBases": lst[37],
                "ontargetReads": lst[38],
                "ontargetBases": lst[39],
                "ontargetBasesRatio": lst[40],
                "oneCoverageRate": lst[41],
                "fourCoverageRate": lst[42],
                "tenCoverageRate": lst[43],
                "twentyCoverageRate": lst[44],
                "fiftyCoverageRate": lst[45],
                "hundredCoverageRate": lst[46],
                "twohundredCoverageRate": lst[47],
                "fivehundredConverageRatemedianDepth": lst[48],
                "medianDepth": lst[49],
                "modeInsertSize": lst[50],
                "minDepth": lst[51],
                "q30": lst[52]
            }
            result.append(item)
    # 关闭文件
    with open(qc_json_file, 'w') as dump_f:
        json.dump(result, dump_f)
    return result

def mutToJson(mut_file,mut_json_file):
    # 文件路径
    path=mut_file
    qc_json_file=mut_json_file
    # 读取文件
    with open(path, 'r', encoding="utf-8") as file:
        # 定义一个用于切割字符串的正则
        seq = re.compile("\t")
        result = []
        # 逐行读取
        next(file)
        for line in file:
            lst = seq.split(line.strip())
            item = {
                "experimentId":lst[0],
                "chr":lst[1],
                "start":lst[2],
                "end":lst[3],
                "ref":lst[4],
                "alt":lst[5],
               "func":lst[6],
                "gene":lst[7],
                "genedetail":lst[8],
                "exonicfunc":lst[9],
                "aachange":lst[10],
                "cytoband":lst[11],
                "genomicsuperdups":lst[12],
                "avsnp150":lst[13],
                "mutationRatio":lst[14],
                "g2015aug":lst[15],
                "cosmic92":lst[16],
                "clnsig":lst[17],
                "clndn":lst[18],
                "clndisdb":lst[19],
                "clnrevstat":lst[20],
                "clnalleleid":lst[21],
                "siftScore":lst[22],
                "siftPred":lst[23],
                "phdivScore":lst[24],
                "phdivPred":lst[25],
                "phvarScore":lst[26],
                "phvarPred":lst[27],
                "lrtScore":lst[28],
                "lrtPred":lst[29],
                "mutationTasterScore":lst[30],
                "mutationTasterPred":lst[31],
                "mutationAssessorScore":lst[32],
                "mutationAssessorPred":lst[33],
                "fathmmScore":lst[34],
                "fathmmPred":lst[35],
                "radialsvmScore":lst[36],
                "radialsvmPred":lst[37],
                "lrScore":lst[38],
                "lrPred":lst[39],
                "vest3Score":lst[40],
                "caddRaw":lst[41],
                "caddPhred":lst[42],
                "gerp":lst[43],
                "phylop46wayPlacental":lst[44],
                "phylop100wayVertebrate":lst[45],
                "siphy29wayLogodds":lst[46],
                "cadd13Rawscore":lst[47],
                "cadd13Phred":lst[48],
                "exac":lst[49],
                "afr":lst[50],
                "amr":lst[51],
                "eas":lst[52],
                "fin":lst[53],
                "nfe":lst[54],
                "oth":lst[55],
                "sas":lst[56],
                "dgvmerged":lst[57],
                "gwascatalog":lst[58],
                "phastconselements46way":lst[59],
                "targetscanS":lst[60],
                "tfbsconssites":lst[61],
                "cg46":lst[62],
                "esp6500si":lst[63],
                "depth":lst[64],
                "oldAachange":lst[66],
                "intervar":lst[67],
                "q20":lst[68],
                "q20PlusOrReduce":lst[69]
            }
            result.append(item)
    # 关闭文件
    with open(qc_json_file, 'w') as dump_f:
        json.dump(result, dump_f)
    return result

if __name__ == '__main__':
    # 请求头
    post_headers = {}
    post_headers[
        'token'] = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYmYiOjE2MzYwMjE1MjYsImlkIjoiMTAwMyIsImV4cCI6MTYzNjAyNTEyNiwiaWF0IjoxNjM2MDIxNTI2fQ.jJC_w83TA-LmP0pecXIkqJddXg6UNAApIcOnI3qyGk0'
    post_headers['Content-Type'] = 'application/json'
    post_headers["Accept"] = "*/*"

    # qc_file = "C:/Users/user/Desktop/test/310.Sequencing.QC.xls"
    # qc_json_file = "C:/Users/user/Desktop/test/310.QCtoJson.json"
    # mut_file="C:/Users/user/Desktop/test/310.mutation.xls"
    # mut_json_file="C:/Users/user/Desktop/test/310.MutationtoJson.json"

    qc_file = sys.argv[1]
    qc_json_file = sys.argv[2]
    mut_file = sys.argv[3]
    mut_json_file = sys.argv[4]
    experimentId = sys.argv[5]

    count = len(open(mut_file, 'r').readlines())
    if count == 1 :
        request_mut = [{
            "experimentId": str(experimentId),
            "chr": "/",
            "start": "/",
            "end": "/",
            "ref": "/",
            "alt": "/"
        }]
    else :
        request_mut = mutToJson(mut_file, mut_json_file)
    print(request_mut)
    request_qc=qcToJson(qc_file,qc_json_file)
    print(request_qc)

    request2qc = getApiInfo_post('http://10.0.1.175', 9001, 'rt/bio-info/batch-receive-qc', post_headers, request_qc)
    print(request2qc)
    request2mut = getApiInfo_post('http://10.0.1.175', 9001, 'rt/bio-info/batch-receive-mutation', post_headers, request_mut)
    print(request2mut)
