<script>
  import fastapi from "../../../lib/api";
  
  export let videoInfo
  
  function post_videoinfo(event) {
    event.preventDefault()
    // console.log(video)
    fastapi('put', '/api/video/input_videoinfo', videoInfo )
  }
  

</script> 

  <b>{videoInfo.id}</b> <br> 

  <div class="ratio ratio-16x9">
    <iframe src="{encodeURIComponent('/video/' + videoInfo.dbid)}" frameborder="0" muted></iframe>
  </div>

  <div class="videoinfo" style="font-size:smaller; white-space: normal; word-break: break-all;">
    
    # {videoInfo.dbid} # {videoInfo.etc}
    # {videoInfo.width}x{videoInfo.height} 
    # {parseInt(videoInfo.showtime/60)}분{videoInfo.showtime%60}초
    # {parseInt(videoInfo.bitrate/1000)}kbps # {parseInt(videoInfo.filesize/1000000)}MB
    # 수정 날자: {videoInfo.date_modified}  # 작성 날자: {videoInfo.date_posted}  # cdate: {videoInfo.cdate}<br>

    
    <form method="post">
      화질 : &nbsp;
      <label>
        <input type="radio" class="form-check-input" bind:group={videoInfo.display_quality} value="아주좋음" >아주좋음 &nbsp;
      </label>
      <label>
        <input type="radio" class="form-check-input" bind:group={videoInfo.display_quality} value="좋음">좋음 &nbsp;
      </label>
      <label>
        <input type="radio" class="form-check-input" bind:group={videoInfo.display_quality} value="보통">보통 &nbsp;
      </label>
      <label>
        <input type="radio" class="form-check-input" bind:group={videoInfo.display_quality} value="흐릿">흐릿 &nbsp;
      </label>
      <label>
        <input type="radio" class="form-check-input" bind:group={videoInfo.display_quality} value="폐기">폐기 &nbsp;
      </label>
      <label>
        <input type="radio" class="form-check-input" bind:group={videoInfo.display_quality} value="del">del &nbsp;
      </label>
      <br>      
      국가 : &nbsp;
      <label>
        <input type="radio" class="form-check-input" bind:group={videoInfo.country} value="한국" >한국 &nbsp;
      </label>
      <label>
        <input type="radio" class="form-check-input" bind:group={videoInfo.country} value="일본">일본 &nbsp;
      </label>
      <label>
        <input type="radio" class="form-check-input" bind:group={videoInfo.country} value="중국">중국 &nbsp;
      </label>
      <label>
        <input type="radio" class="form-check-input" bind:group={videoInfo.country} value="서양">서양 &nbsp;
      </label>
      <label>
        <input type="radio" class="form-check-input" bind:group={videoInfo.country} value="기타">기타 &nbsp;
      </label>
      <label>
        <input type="radio" class="form-check-input" bind:group={videoInfo.country} value="del">del &nbsp;
      </label>
      <br>
      얼굴 : &nbsp;
      <label>
        <input type="radio" class="form-check-input" bind:group={videoInfo.face} value="선명" >선명 &nbsp;
      </label>
      <label>
        <input type="radio" class="form-check-input" bind:group={videoInfo.face} value="흐릿">흐릿 &nbsp;
      </label>
      <label>
        <input type="radio" class="form-check-input" bind:group={videoInfo.face} value="del">del &nbsp;
      </label>
      <br>
      외모 : &nbsp;
      <label>
        <input type="radio" class="form-check-input" bind:group={videoInfo.look} value="마름">마름 &nbsp;
      </label>
      <label>
        <input type="radio" class="form-check-input" bind:group={videoInfo.look} value="보통">보통 &nbsp;
      </label>
      <label>
        <input type="radio" class="form-check-input" bind:group={videoInfo.look} value="뚱">뚱 &nbsp;
      </label>
      <label>
        <input type="radio" class="form-check-input" bind:group={videoInfo.look} value="del">del &nbsp;
      </label>
      <br>
      나이 : &nbsp;
      <label>
        <input type="radio" class="form-check-input" bind:group={videoInfo.age} value="어림" >어림 &nbsp;
      </label>
      <label>
        <input type="radio" class="form-check-input" bind:group={videoInfo.age} value="학생">학생 &nbsp;
      </label>
      <label>
        <input type="radio" class="form-check-input" bind:group={videoInfo.age} value="아가씨">아가씨 &nbsp;
      </label>
      <label>
        <input type="radio" class="form-check-input" bind:group={videoInfo.age} value="아줌마">아줌마 &nbsp;
      </label>
      <label>
        <input type="radio" class="form-check-input" bind:group={videoInfo.age} value="나이많음">나이많음 &nbsp;
      </label>
      <label>
        <input type="radio" class="form-check-input" bind:group={videoInfo.age} value="del">del &nbsp;
      </label>
      <br>
      ㅂㅈ : &nbsp;
      <label>
        <input type="radio" class="form-check-input" bind:group={videoInfo.pussy} value="선명" >선명 &nbsp;
      </label>
      <label>
        <input type="radio" class="form-check-input" bind:group={videoInfo.pussy} value="흐릿">흐릿 &nbsp;
      </label>
      <label>
        <input type="radio" class="form-check-input" bind:group={videoInfo.pussy} value="del">del &nbsp;
      </label>
      
      <br>
      <label>
        <input type="checkbox" bind:value={videoInfo.school_uniform} bind:checked={videoInfo.school_uniform}>교복 &nbsp;
      </label>
      <label>
        <input type="checkbox" bind:value={videoInfo.hip} bind:checked={videoInfo.hip}>엉덩이 &nbsp;
      </label>
      <label>
        <input type="checkbox" bind:value={videoInfo.group} bind:checked={videoInfo.group}>단체 &nbsp;
      </label>
      <label>
        <input type="checkbox" bind:value={videoInfo.pregnant} bind:checked={videoInfo.pregnant}>임신 &nbsp;
      </label>
      <label>
        <input type="checkbox" bind:value={videoInfo.conversation} bind:checked={videoInfo.conversation}>대화 &nbsp;
      </label>
      <label>
        <input type="checkbox" bind:value={videoInfo.lesbian} bind:checked={videoInfo.lesbian}>레즈 &nbsp;
      </label>
      <label>
        <input type="checkbox" bind:value={videoInfo.ani} bind:checked={videoInfo.ani}>에니 &nbsp;
      </label>
      <label>
        <input type="checkbox" bind:value={videoInfo.oral} bind:checked={videoInfo.oral}>입 &nbsp;
      </label>
      <label>
        <input type="checkbox" bind:value={videoInfo.masturbation} bind:checked={videoInfo.masturbation}>자위 &nbsp;
      </label>
      <label>
        <input type="checkbox" bind:value={videoInfo.massage} bind:checked={videoInfo.massage}>마사지 &nbsp;
      </label>
      <label>
        <input type="checkbox" bind:value={videoInfo.uniform} bind:checked={videoInfo.uniform}>회사 &nbsp;
      </label>
      <label>
        <input type="checkbox" bind:value={videoInfo.family} bind:checked={videoInfo.family}>family  &nbsp;
      </label>
      <br>
      <label>
        광고시작 : <input type="number" bind:value={videoInfo.ad_start} placeholder="{videoInfo.ad_start}"/>
      </label> &nbsp; &nbsp;
      <label>
        광고끝 : <input type="number" bind:value={videoInfo.ad_finish} placeholder="{videoInfo.ad_finish}"/>
      </label>
      <br>
      별점 : 
        <select bind:value={videoInfo.star}>
            <option value="1">♥</option>
            <option value="2">♥♥</option>
            <option value="3">♥♥♥</option>
            <option value="4">♥♥♥♥</option>
            <option value="5">♥♥♥♥♥</option>
        </select>
        <b class="text-danger">{"♥".repeat(videoInfo.star)}</b> 
      etc :
      <label>
        <input type="text" bind:value={videoInfo.etc} placeholder="{videoInfo.etc}"/>
      </label><br>
      <input value="등록" type="submit" on:click={post_videoinfo}>
    </form>

  </div>