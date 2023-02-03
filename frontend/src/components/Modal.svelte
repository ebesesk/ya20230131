<script>
  let _video = ''
  let shown = false;
  export function show(video) {
    _video = video
    shown = true;
  }
  export function hide() {
    shown = false;
  }
</script>
<style>
    .modal-wrapper {
        background-color: rgb(0,0,0);
        background-color: rgba(0,0,0,0.6);
        position: fixed;
        width: 100%;
        height: 100%;
        top: 0;
        left: 0;
    }
    .close {
        float: right;
        cursor: pointer;
    }
    .close:hover {
        font-weight: bold;
    }
</style>

{#if shown}
<div class="modal-wrapper">
    <div class="" 
        style="background-color: white;
        max-width: 80vw; 
        padding: 1rem; 
        margin: 15% auto;">
        <span class="close" on:click={() => hide()}>&times;</span>
        <p>{_video.id}</p>
        <slot />
    </div>
</div>
{/if}