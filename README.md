# Google Postmaster Datas

Unofficial tool to download and flatten data from GPT. The recovered data will
offer a simple schema in order to be able to easily save this data in a flat
file or in database.

## Schema

* user_report_spam_percent : `float|None`
* ips_reputations : `list`
* domain_reputation : `level|None`
* feedback_loop : `{ nb_campaigns: 0, percent_per_campaign: list }`
* auth_use_dkim_percent : `float|None`
* auth_use_spf_percent : `float|None`
* auth_use_dmarc_percent : `float|None`
* tls_inbound_percent : `float|None`
* delivery_errors : `list`
* domain : `str`
* date : `str`

### Level

Translates string level from GTP to int

| EN     | FR              | int |
|:------:|:---------------:|:---:|
| high   | bonne           | 4   |
| medium | moyenne         | 3   |
| low    | plutôt mauvaise | 2   |
| bad    | mauvaise        | 1   |
| unknow | unknow          | 0   |

### ips_reputations
  
    [ { 'level': level, 'value': float, 'ips': str } ]

### feedback_loop

    percent_per_campaign : [ { 'uid': int, 'spam_percent': float } ]

# How to use it

```sh
python entry_points_googlepostmasterapi/gpt_dl_all_datas.py -h
> usage: gpt_dl_all_datas [-h] [--token [TOKEN]] [--pool-size [POOL_SIZE]] [--date [DATE]] [--verbose] [--version]
```

```sh
python entry_points_googlepostmasterapi/gpt_dl_domain_datas.py -h
> usage: gpt_dl_domain_datas [-h] [--token [TOKEN]] [--domain [DOMAIN]] [--date [DATE]] [--verbose] [--version]
```

# Support version

Python : `>=3.6`
