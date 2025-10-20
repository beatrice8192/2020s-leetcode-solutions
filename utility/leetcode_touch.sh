# https://github.com/noworneverev/leetcode-api
# curl https://leetcode-api-pied.vercel.app/problem/1

start=$1
end=$2
lang_default=python
ext_default=py
[ -z ${start} ] && exit
[ -z ${end} ] && exit
[ ${start} -gt ${end} ] && exit

for i in {${start}..${end}}; do
    problem=$(curl "https://leetcode-api-pied.vercel.app/problem/${i}" 2>/dev/null | jq "del(.content) | del(.hints) | del(.solution)")
    categoryTitle=$(echo ${problem} | jq -r ".categoryTitle")
    difficulty=$(echo ${problem} | jq -r ".difficulty" | tr '[:upper:]' '[:lower:]')
    isPaidOnly=$(echo ${problem} | jq -r ".isPaidOnly")
    url=$(echo ${problem} | jq -r ".url" | sed "s|/$||g")
    url_file=$(echo ${url} | sed "s|.*/||g")

    if [[ ${categoryTitle} == "Algorithms" ]] || [[ ${categoryTitle} == "Concurrency" ]]; then
        lang=${lang_default}
        ext=${ext_default}
    elif [[ ${categoryTitle} == "Database" ]]; then
        lang=sql
        ext=sql
    elif [[ ${categoryTitle} == "JavaScript" ]]; then
        lang=js
        ext=js
    elif [[ ${categoryTitle} == "Shell" ]]; then
        lang=shell
        ext=sh
    else
        lang=$(echo ${categoryTitle} | tr '[:upper:]' '[:lower:]')
        ext=md
    fi
    if [[ ${isPaidOnly} == "true" ]]; then
        isPaidOnly="-locked"
    else
        isPaidOnly=""
    fi
    dir=$(printf "%04d-%04d${isPaidOnly}-${difficulty}-${lang}" ${start} ${end} | t)
    printf "/"
    file=$(printf "%04d-%s\n" ${i} ${url_file} | t)

    if ! [ -e ${dir}/${file}.${ext} ] && ! [ -e ${dir}/${file}-v1.${ext} ]; then
        mkdir -p ${dir}
        echo "# ${url}" > ${dir}/${file}.${ext}
        git add ${dir}/${file}.${ext}
    fi
done
