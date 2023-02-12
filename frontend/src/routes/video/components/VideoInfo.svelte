<script>
  import fastapi from "../../../lib/api";
  // import { push } from 'svelte-spa-router'
  
  export let video_id
  let video = {}
  let inputs 
  
  function get_video() {
    fastapi ('get', '/api/video/detail/' + video_id, {}, (json) => {
      video = json
      // console.log(video)
      // console.log(video.display_quality)
    })
  }
  get_video()
  
  function post_videoinfo(event) {
    event.preventDefault()
    // console.log(video)
    fastapi('put', '/api/video/input_videoinfo', video )
  }
  

</script> 


  <b>{video.id}</b> <br> 

  <div class="ratio ratio-16x9">
    <iframe src="{encodeURIComponent('/video/' + video.dbid)}" frameborder="0" muted></iframe>
  </div>

  <div class="videoinfo" style="font-size:smaller; white-space: normal; word-break: break-all;">
    
    # {video.dbid} # {video.etc}
    # {video.width}x{video.height} 
    # {parseInt(video.showtime/60)}분{video.showtime%60}초
    # {parseInt(video.bitrate/1000)}kbps # {parseInt(video.filesize/1000000)}MB
    # 수정 날자: {video.date_modified}  # 작성 날자: {video.date_posted}  # cdate: {video.cdate}<br>

    
    <form method="post">
      화질 : &nbsp;
      <label>
        <input type="radio" class="form-check-input" bind:group={video.display_quality} value="아주좋음" >아주좋음 &nbsp;
      </label>
      <label>
        <input type="radio" class="form-check-input" bind:group={video.display_quality} value="좋음">좋음 &nbsp;
      </label>
      <label>
        <input type="radio" class="form-check-input" bind:group={video.display_quality} value="보통">보통 &nbsp;
      </label>
      <label>
        <input type="radio" class="form-check-input" bind:group={video.display_quality} value="흐릿">흐릿 &nbsp;
      </label>
      <label>
        <input type="radio" class="form-check-input" bind:group={video.display_quality} value="폐기">폐기 &nbsp;
      </label>
      <label>
        <input type="radio" class="form-check-input" bind:group={video.display_quality} value="del">del &nbsp;
      </label>
      <br>      
      국가 : &nbsp;
      <label>
        <input type="radio" class="form-check-input" bind:group={video.country} value="한국" >한국 &nbsp;
      </label>
      <label>
        <input type="radio" class="form-check-input" bind:group={video.country} value="일본">일본 &nbsp;
      </label>
      <label>
        <input type="radio" class="form-check-input" bind:group={video.country} value="중국">중국 &nbsp;
      </label>
      <label>
        <input type="radio" class="form-check-input" bind:group={video.country} value="서양">서양 &nbsp;
      </label>
      <label>
        <input type="radio" class="form-check-input" bind:group={video.country} value="기타">기타 &nbsp;
      </label>
      <label>
        <input type="radio" class="form-check-input" bind:group={video.country} value="del">del &nbsp;
      </label>
      <br>
      얼굴 : &nbsp;
      <label>
        <input type="radio" class="form-check-input" bind:group={video.face} value="선명" >선명 &nbsp;
      </label>
      <label>
        <input type="radio" class="form-check-input" bind:group={video.face} value="흐릿">흐릿 &nbsp;
      </label>
      <label>
        <input type="radio" class="form-check-input" bind:group={video.face} value="del">del &nbsp;
      </label>
      <br>
      외모 : &nbsp;
      <label>
        <input type="radio" class="form-check-input" bind:group={video.look} value="마름">마름 &nbsp;
      </label>
      <label>
        <input type="radio" class="form-check-input" bind:group={video.look} value="보통">보통 &nbsp;
      </label>
      <label>
        <input type="radio" class="form-check-input" bind:group={video.look} value="뚱">뚱 &nbsp;
      </label>
      <label>
        <input type="radio" class="form-check-input" bind:group={video.look} value="del">del &nbsp;
      </label>
      <br>
      나이 : &nbsp;
      <label>
        <input type="radio" class="form-check-input" bind:group={video.age} value="어림" >어림 &nbsp;
      </label>
      <label>
        <input type="radio" class="form-check-input" bind:group={video.age} value="학생">학생 &nbsp;
      </label>
      <label>
        <input type="radio" class="form-check-input" bind:group={video.age} value="아가씨">아가씨 &nbsp;
      </label>
      <label>
        <input type="radio" class="form-check-input" bind:group={video.age} value="아줌마">아줌마 &nbsp;
      </label>
      <label>
        <input type="radio" class="form-check-input" bind:group={video.age} value="나이많음">나이많음 &nbsp;
      </label>
      <label>
        <input type="radio" class="form-check-input" bind:group={video.age} value="del">del &nbsp;
      </label>
      <br>
      ㅂㅈ : &nbsp;
      <label>
        <input type="radio" class="form-check-input" bind:group={video.pussy} value="선명" >선명 &nbsp;
      </label>
      <label>
        <input type="radio" class="form-check-input" bind:group={video.pussy} value="흐릿">흐릿 &nbsp;
      </label>
      <label>
        <input type="radio" class="form-check-input" bind:group={video.pussy} value="del">del &nbsp;
      </label>
      
      <br>
      <label>
        <input type="checkbox" bind:value={video.school_uniform} bind:checked={video.school_uniform}>교복 &nbsp;
      </label>
      <label>
        <input type="checkbox" bind:value={video.hip} bind:checked={video.hip}>엉덩이 &nbsp;
      </label>
      <label>
        <input type="checkbox" bind:value={video.group} bind:checked={video.group}>단체 &nbsp;
      </label>
      <label>
        <input type="checkbox" bind:value={video.pregnant} bind:checked={video.pregnant}>임신 &nbsp;
      </label>
      <label>
        <input type="checkbox" bind:value={video.conversation} bind:checked={video.conversation}>대화 &nbsp;
      </label>
      <label>
        <input type="checkbox" bind:value={video.lesbian} bind:checked={video.lesbian}>레즈 &nbsp;
      </label>
      <label>
        <input type="checkbox" bind:value={video.ani} bind:checked={video.ani}>에니 &nbsp;
      </label>
      <label>
        <input type="checkbox" bind:value={video.oral} bind:checked={video.oral}>입 &nbsp;
      </label>
      <label>
        <input type="checkbox" bind:value={video.masturbation} bind:checked={video.masturbation}>자위 &nbsp;
      </label>
      <label>
        <input type="checkbox" bind:value={video.massage} bind:checked={video.massage}>마사지 &nbsp;
      </label>
      <label>
        <input type="checkbox" bind:value={video.uniform} bind:checked={video.uniform}>회사 &nbsp;
      </label>
      <label>
        <input type="checkbox" bind:value={video.family} bind:checked={video.family}>family  &nbsp;
      </label>
      <br>
      <label>
        광고시작 : <input type="number" bind:value={video.ad_start} placeholder="{video.ad_start}"/>
      </label> &nbsp; &nbsp;
      <label>
        광고끝 : <input type="number" bind:value={video.ad_finish} placeholder="{video.ad_finish}"/>
      </label>
      <br>
      별점 : 
        <select bind:value={video.star}>
            <option value="1">♥</option>
            <option value="2">♥♥</option>
            <option value="3">♥♥♥</option>
            <option value="4">♥♥♥♥</option>
            <option value="5">♥♥♥♥♥</option>
        </select>
        <b class="text-danger">{"♥".repeat(video.star)}</b> 
      etc :
      <label>
        <input type="text" bind:value={video.etc} placeholder="{video.etc}"/>
      </label><br>
      <input value="등록" type="submit" on:click={post_videoinfo}>
    </form>



    <!-- {#each Object.entries(video) as [k, v]}
    {#if ! _key.includes(k)}
        {k}  :   {v}<br>
    {/if}
    {/each} -->
  </div>