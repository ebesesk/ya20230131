<script>
import fastapi from "../../../lib/api";

let scanInfo = {

  OverflowError: [],
  NotImplementedError: [],
  FileNotFoundError: [],
  알수없는에러: [],
  db_추가: [],
  converted: [],
  make_gif: [],
  make_webp: [],
  delete_gif:[],
  delet_webp: [],
  delet_dbids: [],
  detect_files: [],
}
// let addInfo = {}

function scan_files() {
    fastapi('get', '/api/video/scan_files', {}, (json) => {
        scanInfo = json
    })
}
scan_files()

// function add_files() {
//     params = {
//         detect_files : scanInfo['detect_files'],
//     }
//     fastapi('post', '/api/video/add_dbids', params, (json) => {
//         addInfo = json
//     })
// }

// function del_db_gif_webp() {
//     fastapi('get', 'api/')
// }
</script>
<div style="font-size: smaller;">
  --------------------------------------------------------------------<br>
  scan 결과<br>
  --------------------------------------------------------------------<br>
  <div style="font-size: smaller;">
    {#each Object.entries(scanInfo) as [k, v]}
    <div style="font-size: smaller;">
      <b>{k} : {v.length}</b><br>  
      <div style="font-size: smaller;">
        {#each v as k}
        {k}
        {/each}
      </div>
      <br>
    </div>
    --------------------------------------------------------------------<br>
    {/each}
  </div>
</div>
<!-- <button  on:click={add_files} style="font-size: smaller;">Add Files</button> -->



