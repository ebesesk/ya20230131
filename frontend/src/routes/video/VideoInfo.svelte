<script>
  export let videoInfo
  console.log(videoInfo)
</script>


<div class="videoinfo" style="font-size:smaller; white-space: normal; word-break: break-all;">
  {#each Object.entries(videoInfo) as [k, v]}
    {#if v != null}
    {k}: {v}<br>
    {/if}
  {/each}
</div>