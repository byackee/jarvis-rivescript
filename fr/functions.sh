#!/bin/bash
# Here you can create functions which will be available from the commands file
# You can also use here user variables defined in your config file
# To avoid conflicts, name your function like this
# jv_pg_XX_myfunction () { }
# jv for JarVis
# pg for PluGin
# XX can be a two letters code for your plugin, ex: ww for Weather Wunderground
jv_pg_pt_lunch()
{
while read device
do
if [[ "$1" == "$device" ]]; then
prog="$(echo "$pourquand" | jq -r ".devices[] | select(.nom==\"$device\") | .voiciladate")"
sh ./plugins/jarvis-progtv/fr/xmltv-tool.sh -p -j cesoir -C $prog ./plugins/jarvis-progtv/tnt.xml
fi
done <<< "$(echo "$pourquand" | jq -r '.devices[].nom')"
}
