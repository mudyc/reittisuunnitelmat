
const get = async url => {
    return new Promise((accept, reject)=> {
        var xhr = new XMLHttpRequest();
        xhr.onload = function () {
            if (xhr.status >= 200 && xhr.status < 300) {
                console.log('success!', xhr);
                accept(JSON.parse(xhr.responseText))
            } else reject(xhr.status)
        };
        xhr.open('GET', url)
        xhr.send()
    })
}

const run = async () => {
    const routes = await get('routes.json')
    routes.map(route =>
         document.body.innerHTML += `<div>${route.name}</div>`
    )
}

run()