import { createClient } from '@supabase/supabase-js';

const supabaseUrl = 'https://dfheqpevgksyxjlxlsce.supabase.co';
const supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRmaGVxcGV2Z2tzeXhqbHhsc2NlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzMxNjQwNDksImV4cCI6MjA4ODc0MDA0OX0.sLrVAja0YTRiB2uWNTs_qRPfbm4FSFa65iifTAHLWuM';

export const supabase = createClient(supabaseUrl, supabaseKey);