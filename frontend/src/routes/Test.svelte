<script>
  import VideoModal from '../components/Modal.svelte'
  let videomodal
  let id = 'ID'
</script>

<style>
  textarea {
    width: 100%;
    height: 90vh;
    background-color: pink;
  }
</style>

<main>
    <textarea/>
    <button on:click={videomodal.show(id)}>Show videomodal</button>
    <VideoModal bind:this={videomodal}>
        <h2>Modal title {id}</h2>
        <p>Modal content</p>
        <button on:click={videomodal.hide()}>Close</button>
    </VideoModal>
</main>