sites=('https://google.com' 'https://facebook.com' 'https://twitter.com')
logfile='website_status.log'

: >$logfile
for item in "${sites[@]}"; do
  status=$(curl -o /dev/null -L -s -w "%{http_code}" "$item")
  if [[ "$status" == "200" ]]; then
    echo "$item is UP" >>$logfile
  else
    echo "$item is DOWN" >>$logfile
  fi
done

echo "successfully loges into $logfile"
