<script>
import fastapi from "../../../lib/api";

let scanInfo = {}
let addInfo = {}

function scan_files() {
    fastapi('get', '/api/video/scan_files', {}, (json) => {
        scanInfo = json
    })
}
scan_files()

function add_files() {
    fastapi('get', '/api/video/add_dbids', {}, (json) => {
        addInfo = json
    })
}

// function del_db_gif_webp() {
//     fastapi('get', 'api/')
// }
</script>
<div style="font-size: smaller;">
    ---------------------------------------------<br>
    scan 결과<br>
    ---------------------------------------------<br>
    {#each Object.entries(scanInfo) as [k, v]}
    {k} :  {v}<br>
    {/each}
    ---------------------------------------------<br>
    추가하기<br>
    ---------------------------------------------<br>
    {#each Object.entries(addInfo) as [k, v]}
    {k} :  {v}<br>
    {/each}
</div>
<button  on:click={add_files()} style="font-size: smaller;">Add Files</button>