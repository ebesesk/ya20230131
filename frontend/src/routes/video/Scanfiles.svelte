<script>
import fastapi from "../../lib/api";

let scanInfo = {}

function scan_files() {
    fastapi('get', '/api/video/scan_files', {}, (json) => {
        scanInfo = json
    })
}
scan_files()
</script>
<div>
    {#each Object.entries(scanInfo) as [k, v]}
    {k}, {v}<br>
    {/each}
</div>