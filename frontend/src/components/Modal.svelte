<script>
  import { createEventDispatcher, onDestroy } from 'svelte';
  const handle_keydown = e => {
    if (e.key === 'Escape') {
      close();
      return;
    }
    
    if (e.key === 'Tab') {
      // trap focus
			const nodes = modal.querySelectorAll('*');
			const tabbable = Array.from(nodes).filter(n => n.tabIndex >= 0);
      
			let index = tabbable.indexOf(document.activeElement);
			if (index === -1 && e.shiftKey) index = 0;
      
			index += tabbable.length + (e.shiftKey ? -1 : 1);
			index %= tabbable.length;
      
			tabbable[index].focus();
			e.preventDefault();
		}
  }
  
  const previously_focused = typeof document !== 'undefined' && document.activeElement;
  
	if (previously_focused) {
    onDestroy(() => {
      previously_focused.focus();
		});
	}
  
  
    

  let _video = ''
  let shown = false;
  export function show() {
    shown = true;
  }
  export function hide() {
    shown = false;
  }
  



</script>

{#if shown}
<div class="modal-wrapper">
  <div 
    class="" 
    style="position: absolute;
           left: 50%;
           top: 50%;
           width: calc(100vw - 4em);
           max-width: 32em;
           max-height: calc(100vh - 4em);
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



<style>
    .modal-wrapper {
        background-color: rgb(0,0,0);
        background-color: rgba(0,0,0,0.7);
        position: fixed;
        /* position: absolute; */
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