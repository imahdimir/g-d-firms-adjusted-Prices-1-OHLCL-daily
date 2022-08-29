"""

  """
##
from githubdata import GithubData
from mirutil.df_utils import read_data_according_to_type as rdata
from mirutil.df_utils import save_as_prq_wo_index as sprq
from mirutil.utils import get_tok_if_accessible as gtok


targ_url = 'https://github.com/imahdimir/d-firms-adjusted-Prices-1-OHLCL-daily'
i2f_url = 'https://github.com/imahdimir/d-TSETMC_ID-2-FirmTicker'

jd = 'JDate'
tid = 'TSETMC_ID'
ftic = 'FirmTicker'

def main() :
  pass
  ##
  rp_targ = GithubData(targ_url)
  ##
  rp_targ.clone()
  ##
  dffp = rp_targ.data_fp
  df = rdata(dffp)
  dfv = df.head()
  ##
  msk = df.duplicated(subset = [jd , tid] , keep = False)
  df1 = df[msk]
  assert df1.empty
  ##
  rp_i2f = GithubData(i2f_url)
  rp_i2f.clone()
  ##
  difp = rp_i2f.data_fp
  di = rdata(difp)
  ##
  di[tid] = di[tid].astype(str)
  df[tid] = df[tid].astype(str)
  ##
  msk =  df[tid].isin(di[tid])
  df = df[msk]
  ##
  df = df.dropna()
  ##
  sprq(df, dffp)
  ##
  tokfp = '/Users/mahdi/Dropbox/tok.txt'
  tok = gtok(tokfp)
  ##
  cur_url = 'https://github.com/' + rp_targ.user_name + '/g-' + rp_targ.repo_name
  ##
  msg = 'only firms kept'
  msg +=



  ##


  ##

##
if __name__ == '__main__' :
  main()  ##