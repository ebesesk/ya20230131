<script>
    import fastapi from "../../lib/api";

    export let video_id
    let video = {}
    let inputs 
    let _key = ['id','dbid','width','height','showtime','bitrate','filesize','date_posted','date_modified'] // ,'cdate','display_quality','country','face','look','age','pussy','etc','school_uniform','hip','group','pregnant','conversation','lesbian','ani','oral','masturbation','massage','uniform','family','ad_start','ad_finish','star']

    function get_video() {
    
        fastapi ('get', '/api/video/detail/' + video_id, {}, (json) => {
            video = json

        })
    }

    get_video()
    // console.log(video)

    



    // let inputs
    // function get_inputs() {
    //     for (var i of _key) {
    //         console.log('-------------')
    //         console.log(i)
    //         inputs = videoInfo
    //         delete inputs[i]
    //         // return inputs
    //     }
    // }
    
    // get_inputs()
    // // console.log(videoInfo[_key[1]])
  </script>
  
  
  <div class="videoinfo" style="font-size:smaller; white-space: normal; word-break: break-all;">
    {video_id}<br>{video.id}
    {#each Object.entries(video) as [k, v]}
        {k}  :   {v}<br>
    {/each}
    <!-- {inputs} -->
    <!-- {#each Object.entries(inputs) as [k, v]}
        {k}<br>
    {/each}
    ===========
    {#each Object.entries(videoInfo) as [k, v]}
        {k} : {v} <br>
    {/each} -->
    <!-- {#each Object.entries(videoInfo) as [k, v]}
      {#if typeof(v) === 'number'} 
      숫자   :
      {k}: {v}<br>
      {/if}
      {#if typeof(v) === 'boolean'} 
      boolean  
      {k}: {v}<br>
      {/if}
      {#if typeof(v) === 'string'} 
      문자   :
      {k}: {v}<br>
      {/if}
    {/each} -->
  </div>