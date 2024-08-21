from url_factory import get_pdu_api_url, url_add_footer
from pdu_request import get, post


def get_pdu_measurement_data(api_hd_url, target_id, target='total', measurement_only=True):
    """
    PDUの電力情報を取得

    Args:
        api_hd_url(str): https://pduのアドレス/api/ハードウェアID/

        target(str): total, phase, breaker, outletを指定

        target_id(int): 取得したい要素のID情報

        mesurement_only(bool): 計測値以外のデータを取得するか否か
    
    Returns:
        PDUからのレスポンス
        
    """

    footer = ''

    if target == 'outlet':
        footer = f'{target}/{target_id}'

    else:
        footer = f'entity/{target}{target_id}'

    if measurement_only:
        footer += '/measurement'

    url = url_add_footer(api_hd_url, footer)

    res = get(url)

    return res


if __name__ == '__main__':

    outlet_id = 1 # アウトレットID
    circuit_id = 1 # サーキットID

    pdu_ip_addr = '192.168.7.195' # PDUのIP address

    pdu_hd_id = 'AB3C1E2E990200C3' # PDUのハードウェアID(PDU本体についている個体識別用ID)

    footer = f'dev/{pdu_hd_id}/'

    pdu_api_url = get_pdu_api_url(pdu_ip_addr, footer=footer) # APIとの通信用URLを取得

    # アウトレットのデータ取得
    outlet_data = get_pdu_measurement_data(pdu_api_url, target_id=outlet_id, target='outlet')   
    
    # サーキットのデータ取得
    circuit_data = get_pdu_measurement_data(pdu_api_url, target_id=circuit_id, target='breaker')

    print(f'アウトレットの計測データ: {outlet_data}')
    print(f'サーキットの計測データ: {circuit_data}')