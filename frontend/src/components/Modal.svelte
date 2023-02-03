<script>
  let _video = ''
  let shown = false;
  export function show() {
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
  <div 
    class="" 
    style="
    position: absolute;
    left: 50%;
    top: 50%;
    width: calc(100vw - 4em);
    max-width: 32em;
    max-height: calc(100vh - 14em);
    overflow: auto;
    transform: translate(-50%,-50%);
    padding: 1em;
    border-radius: 0.2em;
    background: white;"
    >
    <span class="close" on:click={() => hide()}>&times;</span>
    <slot />
  </div>
</div>
{/if}